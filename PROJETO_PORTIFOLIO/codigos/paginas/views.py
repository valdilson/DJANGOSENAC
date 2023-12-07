from django.shortcuts import render
from django.http import HttpResponse, HttpRequest



# Create your views here.

def inicio(request:HttpRequest):
    return render(request, "paginas/inicio.html")