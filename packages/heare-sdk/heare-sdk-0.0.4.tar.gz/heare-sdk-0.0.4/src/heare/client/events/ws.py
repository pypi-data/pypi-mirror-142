import base64
import threading
import time
from multiprocessing.pool import ThreadPool
from heare.config import SettingsDefinition, Setting
import logging
from pyee import EventEmitter
from websocket import WebSocketApp

from heare.client.events.message import Message, Serializer, Deserializer


__author__ = 'seanfitz'

logger = logging.getLogger(__name__)


class HeareClientSettings(SettingsDefinition):
    host = Setting(str)
    port = Setting(int)
    handler_path = Setting(str)
    ssl = Setting(bool, default=False)
    basic_user = Setting(str, default=None, required=False)
    basic_password = Setting(str, default=None, required=False)


class HeareClient(EventEmitter):
    def __init__(self, config: HeareClientSettings):
        EventEmitter.__init__(self)
        self.scheme = "wss" if config.ssl.get() else "ws"
        self.host = config.host.get()
        self.port = config.port.get()
        self.handler_path = config.handler_path.get()
        self.reconnect_counter = 1

        # TODO: extract authorization
        self._auth_header = None
        user = config.basic_user.get()
        if user:
            auth_str = user + ":"
            password = config.basic_password.get()
            if password:
                auth_str += password
            self._auth_header = "Authorization: Basic %s " % str(base64.b64encode(bytes(auth_str, 'utf-8')), 'utf-8')

        self.client = self._create_new_connection()
        self.pool = ThreadPool(10)
        self.serializer = Serializer()
        self.deserializer = Deserializer()

    def _create_new_connection(self):
        headers = []
        if self._auth_header:
            headers.append(self._auth_header)
        return WebSocketApp(
            self.scheme + "://" + self.host + ":" + str(self.port) + self.handler_path,
            header=headers,
            on_open=self._on_remote_open,
            on_close=self._on_remote_close,
            on_error=self._on_remote_error,
            on_message=self._on_remote_message)

    def _on_remote_open(self, _):
        logger.info("Connected")
        self.emit("open")
        self.reconnect_counter = 1

    def _on_remote_close(self):
        self.emit("close")

    def _on_remote_error(self, error, _):
        logger.error(error)
        try:
            self.emit('error', error)
            self.client.close()
        except Exception as e:
            logger.error(repr(e))
        sleep_time = self.reconnect_counter
        logger.warning(
            "Disconnecting on error, reconnecting in %d seconds." % sleep_time)
        self.reconnect_counter = min(self.reconnect_counter * 2, 60)
        time.sleep(sleep_time)
        self.client = self._create_new_connection()
        self.run_forever()

    def _on_remote_message(self, _, message):
        try:
            self.emit('message', message)
        except Exception as e:
            logger.exception("wat")
        parsed_message = self.deserializer.deserialize(message)
        self.emit('parsed_message', parsed_message)
        self.pool.apply_async(
            self.emit, (parsed_message.message_type, parsed_message))

    def emit(self, message: Message):
        if (not self.client or not self.client.sock or
                not self.client.sock.connected):
            return
        self.client.send(self.serializer.serialize(message))
        # TODO: should we emit outbound events locally?
        # The interface is different. Maybe this is ok.
        EventEmitter.emit(self, message.message_type, message)

    def run_forever(self, ping_interval=1):
        try:
            logger.info(f"Attempting to connect to {self.client.url}")
            self.client.run_forever(ping_interval=ping_interval)
        except Exception as _:
            logger.exception("Error connecting to server")
        finally:
            logger.info("Client run_forever complete.")

    def close(self):
        self.client.close()


def main():
    logging.basicConfig(level=logging.DEBUG)
    settings = HeareClientSettings.load()
    client = HeareClient(settings)

    def echo(message):
        logger.info(message)

    client.on('message', echo)
    threading.Thread(target=client.run_forever).start()
    while True:
        utterance = input("Utterance: ")
        client.emit(Message(message_type='utterance', data={'text': utterance}))


if __name__ == "__main__":
    main()
