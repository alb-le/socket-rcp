from typing import Tuple, Optional

import config
from src.clients.client_client import ClientClient
from src.rcp_client import RcpClient


def client_handler():
    host = input('What is the host? Leave it blank for default: ') or config.HOST
    port = input('What is the port? Leave it blank for default: ') or config.PORT

    client = ClientClient(host, port)
    RcpClient(client=client).run()


if __name__ == "__main__":
    client_handler()
