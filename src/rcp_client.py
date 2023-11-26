import config
from src.clients.client_client import ClientClient


class RcpClient:
    def __init__(self, client: ClientClient):
        self.client = client

    def run(self):
        print(f'Started RCP as Client. Address: {self.client}')
        print(f'Write a request. Also, you can write "help()":')
        self.client.handshake()
        fn_name, args, kwargs = self.get_input()
        res = self.client.call_fn(fn_name, args, kwargs)
        print(res)
        self.client.close()

    @staticmethod
    def get_input():
        s = input()
        fn_name = s.split('(')[0]
        args = s[len(fn_name)+1:-1].strip(' ').split(',')
        kwargs = {}
        return fn_name, args, kwargs
