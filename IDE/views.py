# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'IDE/home.html')

    
def otro(request):
    return HttpResponse("Hola Anicka, Django web IDE en proceso :)")