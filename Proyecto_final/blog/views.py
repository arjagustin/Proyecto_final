from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import Articuloform, Autorform, Seccionform

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def formulario_articulos(request):
    #    if request.method == "GET":

    mi_formulario = Articuloform()
    contexto = {"formulario": mi_formulario}
    return render(request, "formulario-articulo.html", context=contexto)


#    if request.method == "POST":
#        mi_formulario = Articuloform(request.POST)
#        if mi_formulario.is_valid():


def formulario_secciones(request):
    mi_formulario = Seccionform()
    contexto = {"formulario": mi_formulario}
    return render(request, "formulario-seccion.html", context=contexto)


def formulario_autores(request):
    mi_formulario = Autorform()
    contexto = {"formulario": mi_formulario}
    return render(request, "formulario-autor.html", context=contexto)
