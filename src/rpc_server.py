import json
import traceback

from src.my_functions import MyFunctions
from src.socket_client import SocketClient


class RpcServer:
    def __init__(self, host: str = '127.0.0.1',
                 port: int = 8080,
                 my_functions: MyFunctions = MyFunctions(),
                 socket_client: SocketClient = SocketClient(),
                 ):
        self.__host = host
        self.__port = port
        self.address = (self.__host, self.__port)
        self.socket_client: SocketClient = socket_client
        self.my_functions = my_functions

    def __multithread_handler(self):
        print(f'Managing requests from {self.address}.')
        while True:
            try:
                function_name, args, kwargs = self.socket_client.receive()

            except Exception as ex:
                print(f'[ERROR] Client {self.address} disconnected.')
                print(f'[ERROR] {traceback.print_exc()}')
                break
            print(f'[INFO] {self.address} -> {function_name}({args})')

            try:
                response = self.my_functions[function_name](*args, **kwargs)

            except Exception as ex:
                print(f'[ERROR] {traceback.print_exc()}')
                response = (str(ex))

            self.socket_client.send(response)

        self.socket_client.close()

    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address)
            sock.listen()

            print(f'+ Server {self.address} running')
            while True:
                try:
                    client, address = sock.accept()

                    Thread(target=self.__handle__, args=[client, address]).start()

                except KeyboardInterrupt:
                    print(f'- Server {self.address} interrupted')
                    break
