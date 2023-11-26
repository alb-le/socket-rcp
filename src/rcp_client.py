from src.clients.client_client import ClientClient


class RcpClient:
    def __init__(self, client: ClientClient):
        self.client = client

    def run(self):
        print(f'Started RCP as Client. Address: {self.client}')
        print(f'Write a request. Also, you can write "help" or "exit":')

    while True:
        user_input = input('Function:').split()