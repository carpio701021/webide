import sys
import socket
import random
from .ply_analyzer import PlyAnalyzer
#import json

class SocketClient:

    TCP_IP = '127.0.0.1'
    TCP_PORT = 9770
    BUFFER_SIZE = 1024

    def sendToServer(self, message):
        #try:
        #levantar cliente
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))
        #enviar mensaje
        s.sendall((message+"\n").encode(encoding='UTF-8'))
        s.sendall(('$*@n!ck@*$\n'.encode(encoding='utf_8')))

        #recibir mensaje
        data = bytes()
        lineas = 0
        while True:
            lineas +=1
            r = s.recv(self.BUFFER_SIZE)
            if b'$$$$$$$$$$' in r:
                break
            #print(r)
            data += r

        reciv = data.decode(encoding='UTF-8')
        #print('Respuesta recibida: $$\n'+reciv+'\n$$')
        s.close()
        return reciv
        '''except:
            print('No se pudo comunicar con servidor. Mensaje a enviar:')
            print(message)
            return """
            [
                "paquete": "error",
                "tipo": "comunicacion",
                "msg": "ha ocurrido un error en el envio del mensaje",
                "datos": [
                    {}
                ]
            ] 
            """.format(message)'''
            

    def getRandom(self):
        return random.randrange(1000,9999)

    def login(self,user,passw):
        res = self.sendToServer("""
            [
                "validar": "{}",
                "login": [
                    "usr" : "{}",
                    "pass": "{}"
                ]
            ] 
            """.format(self.getRandom(),user,passw)
        )
        # @todo falta validar user
        return PlyAnalyzer.analizarLogin(res,'login')

    def paquete(self,tipo,instruccion):
        print(tipo)
        if tipo == "arbol":
            return PlyAnalyzer.analizar('res',tipo)
        res = self.sendToServer("""
            [
                "validar": "{}",
                "paquete": "{}",
                "instruccion": ~{}~
            ] 
            """.format(self.getRandom(),tipo, instruccion))
        #analizar respuesta y devolver json con las salidas
        print ("res: "+res)
        return PlyAnalyzer.analizar(res,tipo)



#metodo que devuelve los nombres de tablas y metodos a utilizar


#metodo que devuelve un arbol