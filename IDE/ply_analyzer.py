import socket
import random
#import json

class PlyAnalyzer:

    
    @staticmethod
    def analizarLogin(respuesta):
        
        #aqui se analiza

        ##pruebas que estoy haciendo
        return { 'resultado': True, 'usuario': 'user', 'isAdmin': False }

   
    @staticmethod
    def analizar(respuesta):
        
        #aqui se analiza

        ##pruebas que estoy haciendo
        ##si es de tipo login
        if '"paquete": "usql",' in respuesta :
            return {
                'salida'    : respuesta + '\n',
                'plan'      : 'Desde el backend hasta el plan de ejecucion' + '\n\n',
                'mensajes'  : 'Desde el backend hasta los mensajes XD ' + '\n\n',
                'historial' : 'Desde el backend hasta el historial' + '\n\n'
            }
        elif '"paquete": "reporte",' in respuesta:
            return {
                'resultado'    : respuesta.replace('<usql>','<usql id="codigo nuevo">') + '\n'
            }
        elif '"paquete": "arbol",' in respuesta:
            return {
                'arbol'    : 'Aqui devuelvo el mega arbol\n'
            }
        elif '"paquete": "",' in respuesta:
            return 'vacio'
        return 'blah'

