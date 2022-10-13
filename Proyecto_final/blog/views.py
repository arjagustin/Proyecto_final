from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import Articuloform, Autorform, Seccionform

# Create your views here.


def inicio(request):
    return render(request, "/inicio.html")


def formulario_articulos(request):
    mi_formulario: Articuloform()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-articulo.html", context=contexto)


def formulario_secciones(request):
    mi_formulario: Seccionform()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-seccion.html", context=contexto)


def formulario_autores(request):
    mi_formulario: Autorform()
    contexto = {"formulario": mi_formulario}
    return render(request, "blog/formulario-autor.html", context=contexto)
