import json
import socket
from typing import List

import config
from src.clients.client import Client
from src.my_exception import DisconnectedException


class ServerClient(Client):
    def __init__(self, host: str = None, port: int = None):
        super().__init__(host, port)

    @staticmethod
    def get_address(socket_: socket.socket) -> str:
        socket_address = socket_.getsockname()
        return f'{socket_address[0]}:{socket_address[1]}'

    @staticmethod
    def send(socket_: socket.socket, payload: str):
        socket_.sendall(json.dumps(payload).encode())

    @staticmethod
    def receive_to_worker(worker_socket: socket.socket) -> list:
        res = json.loads(worker_socket.recv(config.MSG_SIZE).decode())
        if not res:
            raise DisconnectedException
        return res

    @staticmethod
    def close_worker_socket(worker_socket: socket.socket):
        worker_socket.close()
