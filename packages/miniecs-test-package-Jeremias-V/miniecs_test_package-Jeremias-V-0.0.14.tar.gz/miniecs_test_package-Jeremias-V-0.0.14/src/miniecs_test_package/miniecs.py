import socket
from xmlrpc.client import Boolean

class MiniECS:
    """
    A class used to define the methods of the mini elastic
    container service project for Operating Systems course.

    _______________________________________________________

    Methods:

    - create_container(name="CONTAINER_NAME") -> RESPONSE
      This method allows the user to create a container.

    - list_containers()

    - stop_container()

    - delete_instance()

    """

    def __init__(self, address = 'localhost', port = 65535) -> None:
        self.address = address
        self.port = port
        self.sock = socket.create_connection((self.address, self.port))
        self.containers_list = []

    def stop(self):
        self.sock.close()

    def create_container(self, name: str):

        response = (False, "None")

        if name not in self.containers_list:

            self.containers_list.append(name)

            try:
                # Send data
                message = name.encode()
                print('sending {!r}'.format(message))
                self.sock.sendall(message)

                amount_received = 0
                amount_expected = len(message)
                while amount_received < amount_expected:
                    data = self.sock.recv(16)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

            finally:
                response = (True, "Success, the container with name '{}' was created.".format(name))
        
        else:

            response = (False, "Error, the container with name '{}' already exists.".format(name))
        
        return response
    
    def list_containers(self) -> str:
        return self.containers_list

    def stop_container(self, name: str) -> str:
        pass

    def delete_instance(self, name: str) -> str:
        pass
