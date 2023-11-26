import socket
import traceback
from threading import Thread
from typing import Tuple

from src.clients.server_client import ServerClient
from src.my_exception import DisconnectedException
from src.server_functions import FunctionsImplementation


class RcpServer:
    def __init__(self, client: ServerClient, my_functions: FunctionsImplementation):
        self.client: ServerClient = client
        self.my_functions = my_functions

    def __multithread_handler(self, worker_socket: socket.socket, address: Tuple[str, int]):
        try:
            print(f'Managing requests from {address}.')
            while True:

                try:
                    request = self.client.receive_to_worker(worker_socket)
                    print(f'[INFO] {self.client.get_address(worker_socket)} -> Request: {request}.')
                    response = self.my_functions.run_fn(request)

                except DisconnectedException:
                    print(f'[INFO] Client {self.client.get_address(worker_socket)} disconnected.')
                    break

                except Exception as ex:
                    print(f'[ERROR] {str(ex)}\n\n{traceback.print_exc()}')
                    response = (str(ex))
                    raise ex

                self.client.send(socket_=worker_socket, payload=response)
        finally:
            self.client.close_worker_socket(worker_socket)

    def run(self) -> None:
        self.client.start_listening()
        while True:
            try:
                client, address = self.client.accept()
                Thread(target=self.__multithread_handler, args=[client, address]).start()

            except KeyboardInterrupt:
                self.client.close()
                print(f'- Server {self.client} interrupted.')
                break

            except Exception as ex:
                self.client.close()
                raise ex
