# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .socket_client import SocketClient

@csrf_exempt
def login(request):
    server = SocketClient()
    print(server.sendToServer('[ "paquete":"fin"]')) #aqui se cierra la sesion
    request.session['login'] = ''
    request.session['admin'] = ''
    if request.method == 'GET':
        return render(request, 'IDE/login.html')
    elif request.method == 'POST':
        #confirmar datos en el server
        if( request.POST['user'] == 'admin' and request.POST['password'] == 'admin'):
            print('Login exitoso')
            #establecer cookie
            request.session['login'] = request.POST['user']
            request.session['admin'] = 'true'
            return redirect('index')
        else:
            resLogin = server.login( request.POST['user'],request.POST['password']) 
            if (resLogin['resultado']):
                print('Login exitoso')
                #establecer cookie
                request.session['login'] = resLogin['usuario']
                request.session['admin'] = resLogin['isAdmin']
                return redirect('index')

    
    return render(request, 'IDE/login.html', {'error': '<i class="fa fa-close"></i> Error, usuario o contraseña inválidos'})
    

def index(request):
    #leer cookie
    if( not request.session.get('login', False) ):
        #si no hay login redireccionar a login
        return redirect('login')
    
    return render(request, 'IDE/home.html', {'user': request.session['login'], 'admin': request.session['admin']})


def newScriptPanel(request):
    numPanel = request.GET['numPanel']
    return render(request,'IDE/components/scriptPanel.html' , {'numPanel':numPanel})

def newScriptPanelTab(request):
    numPanel = request.GET['numPanel']
    return render(request,'IDE/components/scriptPanelTab.html' , {'numPanel':numPanel})

def newReportPanel(request):
    numPanel = request.GET['numPanel']
    return render(request,'IDE/components/reportPanel.html' , {'numPanel':numPanel})

def newReportPanelTab(request):
    numPanel = request.GET['numPanel']
    return render(request,'IDE/components/reportPanelTab.html' , {'numPanel':numPanel})

@csrf_exempt
def executeScript(request):
    sqlCode = request.POST['sqlcode']
    server = SocketClient()
    respuesta = server.paquete( 'usql', sqlCode )
    #a = parser.parse('[paquete: "c1", datos: "c2", ejecucion: "c3", mensaje: "c4", historial: "c5"]')

    
    #esta variable respuesta es la que debe ser parseada para generar luego el json


    #aqui un json de ejemplo para la respuesta
    return JsonResponse(respuesta,safe=False)
    #return JsonResponse({
    #    'salida'    : respuesta + '\n',
    #    'plan'      : 'Desde el backend hasta el plan de ejecución' + '\n\n',
    #    'mensajes'  : 'Desde el backend hasta los mensajes XD ' + '\n\n',
    #    'historial' : 'Desde el backend hasta el historial' + '\n\n'
    #})

@csrf_exempt
def executeReport(request):
    sqlCode = request.POST['sqlcode']
    server = SocketClient()
    respuesta = server.paquete('reporte', sqlCode )


    #aqui un json de ejemplo para la respuesta
    return JsonResponse(respuesta)

@csrf_exempt
def getCodigo(request):
    nombre = request.GET['nombre']
    server = SocketClient()
    respuesta = server.paquete('get_codigo_bd', nombre )
    return JsonResponse({'codigo' : respuesta})

@csrf_exempt
def showReport(request):
    htmlcode = request.POST['htmlcode']
    htmlcode = htmlcode.replace("<table", "<table border=1")
    return render(request,'IDE/reportView.html' , {'htmlcode':htmlcode})

def getDbTree(request):
    server = SocketClient()
    respuesta = server.paquete('arbol', '' )
    return JsonResponse ({"respuesta":respuesta})
    '''return HttpResponse("""
[
    {

        "text": "<span class='cm-databases'>Bases de datos</span>",
        "icon": "fa fa-database",
        "nodes" : [
            {
                "text": "<span class='cm-database' db='$db_id'>BD_1</span>",
                "icon": "fa fa-database",
                "nodes" : [
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
            },
            {
                "text": "BD FISQL"
            },
            {
                "text": "BD 3"
            },
            {
                "text": "Base de datos prueba"
            },
            {
                "text": "BD prueba 5"
            }
    
        ]
    },
     {

        "text": "<span class='cm-users'>Usuarios</span>",
        "icon": "fa fa-user",
        "nodes" : [
            {
                "text": "<span class='cm-user'>Anicka</span>",
                "icon": "fa fa-user"
            },
            {
                "text": "<span class='cm-user'>Michelle</span>",
                "icon": "fa fa-user"
            }
        ]

    }

]
    """)'''