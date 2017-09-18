import socket
import random
import json

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
            arbol_txt = """{
	"databases": [
		{
			"database_id": "base_1",
			"tables": [
				{
					"table_id": "tabla_1",
					"columns": [
						"columna1", "columna2","columna3","columna4"
					]
				},
				{
					"table_id": "tabla_2",
					"columns": [
						"columna1", "columna2","columna3","columna4"
					]
				}
			],
			"functions": ["funcion1","funcion2","funcionX"],
			"objects": ["obj1","obj2","superobjeto"]
		},
		{
			"database_id": "FISQL_DB",
			"tables": [
				{
					"table_id": "tabla_prueba",
					"columns": [
						"columna1", "columna2","columna3","columna4"
					]
				}
			],
			"functions": ["funcion1","funcion2","funcionX"],
			"objects": ["obj1","obj2","superobjeto"]
		}
	],
	"users": [
		"admin","anicka","michelle","byron"
	]
}"""


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
                            "icon": "fa fa-code"
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