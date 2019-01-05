from socket import socket
from threading import Thread


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.server = socket()

    def run(self):
        pass

    def accept(self):
        connection, address = self.server.accept()
        self.listen(connection)

    def listen(self, connection):
        while True:
            message = connection.recv(1024)
            print(message)



if __name__ == "__main__":
    pass
