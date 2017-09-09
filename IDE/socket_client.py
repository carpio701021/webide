import socket

class socket_client:
    
    TCP_IP = '127.0.0.1'
    TCP_PORT = 9770
    BUFFER_SIZE = 1024

    def sendToServer(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        s.send(message)
        data = s.recv(self.BUFFER_SIZE)
        s.close()
        return data