import config
from src.clients.server_client import ServerClient
from src.server_functions import FunctionsImplementation
from src.rcp_server import RcpServer


def server_handler():
    client = ServerClient(host=config.HOST, port=config.SERVER_PORT)
    fn = FunctionsImplementation()
    RcpServer(client=client, my_functions=fn).run()


if __name__ == "__main__":
    server_handler()
