from django.contrib import admin
from django.urls import path, include


from blog.views import (
    inicio,
    MyLogin,
    MyLogout,
    formulario_articulos,
    formulario_autores,
    formulario_categoria,
    buscar_articulo,
    buscar_categoria,
    buscar_autor,
    register
)

urlpatterns = [
    path("inicio/", inicio),
    path("inicio/login.html/", MyLogin.as_view(), name="login"),
    path("inicio/logout.html/", MyLogout.as_view(), name="logout"),
    path("inicio/register.html/", register, name="register"),
    path("inicio/formulario-articulo.html/", formulario_articulos),
    path("inicio/formulario-seccion.html/", formulario_categoria),
    path("inicio/formulario-autor.html/", formulario_autores),
    path("inicio/formulario-busqueda-articulo.html/", buscar_articulo),
    path("inicio/formulario-busqueda-seccion.html/", buscar_categoria),
    path("inicio/formulario-busqueda-autor.html/", buscar_autor),
]
