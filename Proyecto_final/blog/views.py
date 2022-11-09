from multiprocessing import context
from operator import is_not
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import Articuloform, Autorform, Categoriaform, Registrousuario
from blog.models import Articulo, Categoria, Autor
from datetime import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.auth.models import User

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


def formulario_categoria(request):
    if request.method == "GET":

        mi_formulario = Categoriaform()
        contexto = {"formulario": mi_formulario}
        return render(request, "formulario-seccion.html", context=contexto)

    if request.method == "POST":

        mi_formulario = Categoriaform(request.POST)
        if mi_formulario.is_valid():
            mi_formulario_completado = mi_formulario.cleaned_data
            nuevo_articulo = Categoria(
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


def buscar_articulo(request):
    if request.method == "GET":
        return render(request, "formulario-busqueda-articulo.html")

    if request.method == "POST":
        titulo_a_buscar = request.POST["titulo"]
        resultados_de_busqueda = Articulo.objects.filter(titulo=titulo_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "resultado-busqueda-articulo.html", context=contexto)


def buscar_categoria(request):
    if request.method == "GET":
        return render(request, "formulario-busqueda-seccion.html")

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"]
        resultados_de_busqueda = Categoria.objects.filter(nombre=nombre_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "resultado-busqueda-seccion.html", context=contexto)


def buscar_autor(request):
    if request.method == "GET":
        return render(request, "formulario-busqueda-autor.html")

    if request.method == "POST":
        nombre_a_buscar = request.POST["nombre"]
        resultados_de_busqueda = Autor.objects.filter(nombre=nombre_a_buscar)
        contexto = {"resultados": resultados_de_busqueda}
        return render(request, "resultado-busqueda-autor.html", context=contexto)


class MyLogin(LoginView):
    template_name = "blog/inicio/login.html"

class MyLogout(LogoutView):
    template_name = "blog/inicio/logout.html"

def register(request):
    if request.method == 'POST':
        form = Registrousuario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} registrado')
            return redirect('feed')
    else:
        form = Registrousuario()

    context = {'form': form}
    return render(request, 'blog/registro.html', context)
    

def mostrar_inicio(request):
    return render(request, "blog/inicio.html")