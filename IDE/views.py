# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
def executeScript(request):

    salida = "Desde el backend hasta la salida de datos :):\n" + request.POST['sqlcode']


    return JsonResponse({
        'salida'    : salida + '\n',
        'plan'      : 'Desde el backend hasta el plan de ejecución' + '\n\n',
        'mensajes'  : 'Desde el backend hasta los mensajes XD ' + '\n\n',
        'historial' : 'Desde el backend hasta el historial' + '\n\n'
    })

    ##return HttpResponse("Hola Codigo, Django web IDE en proceso :):\n" + request.POST['sqlcode'])

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