from multiprocessing import context
from operator import is_not
from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import Articuloform, Autorform, Seccionform
from blog.models import Articulo, Seccion, Autor
from datetime import datetime

# Create your views here.


def inicio(request):
    return render(request, "inicio.html")


def formulario_articulos(request):
    if request.method == "GET":
        mi_formulario = Articuloform()
        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-articulo.html", context=contexto)

    if request.method == "POST":

        mi_formulario = Articuloform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Articulo(
                titulo=mi_formulario_completado["titulo"],
                articulo=mi_formulario_completado["articulo"],
                fecha_de_publicacion=mi_formulario_completado["fecha_de_publicacion"],
            )
            nuevo_articulo.save()
            return render(request, "formulario_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-articulo.html", context=contexto)


def formulario_secciones(request):
    if request.method == "GET":

        mi_formulario = Seccionform()
        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-seccion.html", context=contexto)

    if request.method == "POST":

        mi_formulario = Seccionform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Seccion(
                nombre=mi_formulario_completado["nombre"],
                fecha_de_creacion=mi_formulario_completado["fecha_de_creacion"],
            )
            nuevo_articulo.save()
            return render(request, "formulario_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-seccion.html", context=contexto)


def formulario_autores(request):
    if request.method == "GET":

        mi_formulario = Autorform()
        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-autor.html", context=contexto)

    if request.method == "POST":

        mi_formulario = Autorform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Autor(
                nombre=mi_formulario_completado["nombre"],
                apodo=mi_formulario_completado["apodo"],
                profecion=mi_formulario_completado["profecion"],
                edad=mi_formulario_completado["edad"],
                mail=mi_formulario_completado["mail"],
            )
            nuevo_articulo.save()
            return render(request, "formulario_exitoso.html")

        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-autor.html", context=contexto)
