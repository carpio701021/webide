import socket
import random
import json
from IDE.analisis_sintactico_usr import parser
from IDE.Login import Login

class PlyAnalyzer:

    
    @staticmethod
    def analizarLogin(respuesta,instruccion):
        
        res= True
        estado= ''
        usr= ''
        #aqui se analiza
        #a= parser.parse('[login:"True"  usr:"Anicka"]')
        a= parser.parse(respuesta)
        if (a):
            estado = a.estado
            usr = a.usr
            print('trae informacion')
        else:
            print('No trae informacion')

    
        estado= estado.replace('"','')
        usr= usr.replace('"','')
        print(estado)
        print(usr)

        if (estado=='True'):
            res=True
        else:
            res=False

        print(res)
        ##pruebas que estoy haciendo
        return { 'resultado': res, 'usuario': usr, 'isAdmin': False }

   
    @staticmethod
    def analizar(respuesta,tipo):
        print (tipo)
        print (tipo== 'usql')
        if tipo == 'usql':
        
            #aqui se analiza
            #a = parser.parse(respuesta)
            #print(respuesta)    
            x = json.loads(respuesta)
            print (x)
            

        ##pruebas que estoy haciendo
        ##si es de tipo login
        #if '"paquete": "usql",' in respuesta :
            return {
                'salida'    : x['datos'] + '\n',
                'plan'      : x['ejecucion'] + '\n\n',
                'mensajes'  : x['mensaje'] + '\n\n',
                'historial' : x['historial'] + '\n\n'
            }
        
        if tipo == 'reporte':
            return {
                'resultado'    :  json.loads(respuesta)['datos'] + '\n'
            }
        
        if tipo == 'arbol':
            arbol_txt = respuesta
            print('request from tree')
            print(respuesta)
            #print (palabras_sugeridas)
            return {
                'arbol'    : PlyAnalyzer.generarArbol_cm(arbol_txt),
                'tables'   : PlyAnalyzer.palabras_sugeridas(arbol_txt)
            }
        elif '"paquete": "",' in respuesta:
            return 'vacio'
        return 'blah'


    @staticmethod
    def palabras_sugeridas(json_txt):
        jsdb = json.loads(json_txt)
        palabras_sugeridas = ''
        jsres = {}

        for database in jsdb['databases']:
            palabras_sugeridas += ' '
            palabras_sugeridas += database['database_id']
            jsres[database['database_id']]= {}
            for table in database['tables'] :
                palabras_sugeridas += ' '
                palabras_sugeridas += table['table_id']
                jsres[table['table_id']]= {}
                for column in table['columns'] :
                    palabras_sugeridas += ' '
                    palabras_sugeridas += column
                    jsres[column]= {}
            for function in database['functions'] :
                palabras_sugeridas += ' '
                palabras_sugeridas += function
                jsres[function]= {}
            for nobject in database['objects'] :
                palabras_sugeridas += ' '
                palabras_sugeridas += nobject
                jsres[nobject]= {}
        for user in jsdb['users']:
            palabras_sugeridas += ' '
            palabras_sugeridas += user
            jsres[user]= {}

        return jsres

    @staticmethod
    def generarArbol_cm(json_txt):
        jsdb = json.loads(json_txt)
        jstree = ''

        #analizar bases de datos
        jstree += """
[
    {
        "text": "<span class='cm-databases'>Bases de datos</span>",
        "icon": "fa fa-database",
        "nodes" : ["""
        contadorDatabases = 0
        for database in jsdb['databases'] :
            if contadorDatabases > 0 :
                jstree += ","
            contadorDatabases += 1
            jstree += """
            {
                "text": "<span class='cm-database' db='$database_id'>$database_id</span>",
                "icon": "fa fa-database",
                "nodes" : [
                    {
                        "text": "<span class='cm-tables' db='$database_id'>Tablas</span>",
                        "icon": "fa fa-table",
                        "nodes": [""".replace("$database_id",database['database_id'])
            
            contadorTables = 0
            for table in database['tables'] : 
                if contadorTables > 0 :
                    jstree += ","
                contadorTables += 1
                jstree += """
                            {
                            "text": "<span class='cm-table' db='$database_id' table='$table_id'>$table_id</span>",
                            "icon": "fa fa-table"
                            }""".replace("$database_id",database['database_id']).replace("$table_id",table['table_id'])
                contadorColumns = 0
                for column in table['columns'] : 
                    #if contadorColumns > 0 :
                        #jstree += ","
                    contadorColumns += 1
                    jstree += """"""


            #cierra tables
            jstree +="""
                        ]
                    },"""
            
            #abre functions
            jstree += """
                    {
                        "text": "<span class='cm-functions' db='$database_id'>Funciones</span>",
                        "icon": "fa fa-code",
                        "nodes": [""".replace("$database_id",database['database_id'])
            
            contadorFunctions = 0
            for function in database['functions'] : 
                if contadorFunctions > 0 :
                    jstree += ","
                contadorFunctions += 1
                jstree += """
                            {
                            "text": "<span class='cm-function' db='$database_id' function='$function_id'>$function_id</span>",
                            "icon": "fa fa-code"
                            }""".replace("$database_id",database['database_id']).replace("$function_id",function)

            #cierra functions
            jstree +="""
                        ]
                    },"""
            
            #abre procedures
            jstree += """
                    {
                        "text": "<span class='cm-procedures' db='$database_id'>Procedimientos</span>",
                        "icon": "fa fa-code",
                        "nodes": [""".replace("$database_id",database['database_id'])
            
            contadorprocedure = 0
            for procedure in database['procedures'] : 
                if contadorprocedures > 0 :
                    jstree += ","
                contadorprocedures += 1
                jstree += """
                            {
                            "text": "<span class='cm-procedure' db='$database_id' procedure='$procedure_id'>$procedure_id</span>",
                            "icon": "fa fa-code"
                            }""".replace("$database_id",database['database_id']).replace("$procedure_id",procedure)

            #cierra procedures
            jstree +="""
                        ]
                    },"""
            

            #abre objects
            jstree += """
                    {
                        "text": "<span class='cm-objects' db='$database_id'>Objetos</span>",
                        "icon": "fa fa-cube",
                        "nodes": [""".replace("$database_id",database['database_id'])
            
            contadornobject = 0
            for nobject in database['objects'] : 
                if contadornobject > 0 :
                    jstree += ","
                contadornobject += 1
                jstree += """
                            {
                            "text": "<span class='cm-object' db='$database_id' object='$nobject'>$nobject</span>",
                            "icon": "fa fa-cube"
                            }""".replace("$database_id",database['database_id']).replace("$nobject",nobject)
            #cierra objects
            jstree +="""
                        ]
                    }"""

            

            #cierra database
            jstree +="""
                ]
            }"""

        #cierra databases
        jstree +="""
        ]
    },"""

    
        #abre users
        jstree +="""
    {

        "text": "<span class='cm-users'>Usuarios</span>",
        "icon": "fa fa-user",
        "nodes" : ["""
        contadorUsers = 0
        for user in jsdb['users'] : 
            if contadorUsers > 0 :
                jstree += ","
            contadorUsers += 1
            jstree += """
            {
                "text": "<span class='cm-user' user='$user_id'>$user_id</span>",
                "icon": "fa fa-user"
            }""".replace('$user_id',user)

        #cierra users
        jstree +="""
        ]
    }"""
        #cierra json
        jstree +="""
]"""

        xx ="""
                    {
                        "text": "<span class='cm-tables' db='$db_id'>Tablas</span>",
                        "icon": "fa fa-table",
                        "nodes": [
                            {
                            "text": "<span class='cm-table' db='BD_1' table='$tabla_id'>Tabla 1</span>",
                            "icon": "fa fa-table"
                            },
                            {
                            "text": "<span class='cm-table' db='DB_1' table='$table_id>Tabla 2</span>",
                            "icon": "fa fa-table"
                            }
                        ]
                    },
                    {
                        "text": "<span class='cm-procedures' db='DB_1'>Procedimientos</span>",
                        "icon": "fa fa-code",
                        "nodes": [
                            {
                            "text": "<span class='cm-procedure' db='BD_1'>Procedimiento_1</span>",
                            "icon": "fa fa-code"
                            },
                            {
                            "text": "<span class='cm-procedure' db='DB_1'>Procedimiento_2</span>",
                            "icon": "fa fa-code"
                            }
                        ]
                    },
                    {
                        "text": "<span class='cm-objects' db='BD_1'>Objetos</span>",
                        "icon": "fa fa-cube",
                        "nodes": [
                            {
                            "text": "<span class='cm-object' db='BD_1'>Objeto_1</span>",
                            "icon": "fa fa-cube"
                            },
                            {
                            "text": "<span class='cm-object' db='DB_1'>Mi_objeto_2</span>",
                            "icon": "fa fa-cube"
                            }
                        ]
                    }
                ]
            }
            """
        return jstree
        #analizar usuarios