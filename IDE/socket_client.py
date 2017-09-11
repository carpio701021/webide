import socket

class SocketClient:

    TCP_IP = '127.0.0.1'
    TCP_PORT = 9770
    BUFFER_SIZE = 1024

    def sendToServer(self, message):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        s.sendall((message+"\n").encode(encoding='UTF-8'))
        s.sendall(('$$$$$*$*$*$*****$$$$$\n'.encode(encoding='utf_8')))
        data = s.recv(self.BUFFER_SIZE)
        print('Data recibida: _'+data.decode(encoding='UTF-8')+'_')
        s.close()
        return data.decode(encoding='UTF-8')
