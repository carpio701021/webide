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
    s = SocketClient()
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
        elif (s.login(request.POST['user'],request.POST['password'])):
            print('Login exitoso')
            #establecer cookie
            request.session['login'] = s.user
            request.session['admin'] = s.isAdmin
            return redirect('index')

    
    return render(request, 'IDE/login.html', {'error': '<i class="fa fa-close"></i> Error, usuario o contraseña inválidos'})
    

def index(request):
    #leer cookie
    if( not request.session.get('login', False) ):
        #si no hay login redireccionar a login
        return redirect('login')
    
    return render(request, 'IDE/home.html', {'user': request.session['login'], 'admin': request.session['admin']})

    
def otro(request):
    return HttpResponse("Hola Anicka, Django web IDE en proceso :)")

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
    s = SocketClient()
    respuesta = s.usql( sqlCode )
    #esta variable respuesta es la que debe ser parseada para generar luego el json


    #aqui un json de ejemplo para la respuesta
    return JsonResponse({
        'salida'    : respuesta + '\n',
        'plan'      : 'Desde el backend hasta el plan de ejecución' + '\n\n',
        'mensajes'  : 'Desde el backend hasta los mensajes XD ' + '\n\n',
        'historial' : 'Desde el backend hasta el historial' + '\n\n'
    })

@csrf_exempt
def executeReport(request):
    sqlCode = request.POST['sqlcode']
    #s = SocketClient()
    #respuesta = s.sendToServer( sqlCode )
    #esta variable respuesta es la que debe ser parseada para generar luego el json


    #aqui un json de ejemplo para la respuesta
    return JsonResponse({
        'resultado'    : sqlCode.replace('<usql>','<usql id="codigo nuevo">') + '\n'
    })

@csrf_exempt
def showReport(request):
    htmlcode = request.POST['htmlcode']
    htmlcode = htmlcode.replace("<table", "<table border=1")
    return render(request,'IDE/reportView.html' , {'htmlcode':htmlcode})

def getDbTree(request):
    return HttpResponse("""
[
    {

        "text": "<span class='cm-databases'>Bases de datos</span>",
        "icon": "fa fa-database",
        "nodes" : [
            {
                "text": "<span class='cm-database' db='DB_1'>BD_1</span>",
                "icon": "fa fa-database",
                "nodes" : [
                    {
                        "text": "<span class='cm-tables' db='DB_1'>Tablas</span>",
                        "icon": "fa fa-table",
                        "nodes": [
                            {
                            "text": "<span class='cm-table' db='BD_1'>Tabla 1</span>",
                            "icon": "fa fa-table"
                            },
                            {
                            "text": "<span class='cm-table' db='DB_1'>Tabla 2</span>",
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
    """)