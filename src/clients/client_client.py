from src.clients.client import Client


class ClientClient(Client):
    def __init__(self, host: str = None, port: int = None):
        super().__init__(host, port)
