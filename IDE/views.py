# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .socket_client import SocketClient

def index(request):
    return render(request, 'IDE/home.html')

    
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
    respuesta = s.sendToServer( sqlCode )
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
            "text": "BD 1",
            "icon": "fa fa-database",
            "nodes" : [
                {
                    "text": "Tablas",
                    "icon": "fa fa-table",
                    "nodes": [
                        {
                        "text": "Tabla 1",
                        "icon": "fa fa-table"
                        },
                        {
                        "text": "Tabla 2",
                        "icon": "fa fa-table"
                        }
                    ]
                },
                {
                    "text": "Procedimientos",
                    "icon": "fa fa-code"
                },
                {
                    "text": "Objetos",
                    "icon": "fa fa-cube"
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
    """)