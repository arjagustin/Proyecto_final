from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def inicio(request):
    pass


def formulario_articulos(request):
    return render(request, "blog/formulario-articulos.html")


def formulario_secciones(request):
    return render(request, "blog/formulario-secciones.html")


def formulario_autores(request):
    return render(request, "blog/formulario-aautores.html")
