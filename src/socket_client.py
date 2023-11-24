import json
import socket
from typing import Tuple

import config


class SocketClient:
    def __init__(self):
        self.client: socket.socket = socket

    def connect(self, adrass: Tuple[str, int]):
        NotImplemented

    def send(self, payload: str):
        self.client.sendall(json.dumps(payload).encode())

    def receive(self):
        json.loads(self.client.recv(config.SIZE).decode())

    def close(self):
        self.client.close()
