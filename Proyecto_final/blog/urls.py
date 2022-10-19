from django.contrib import admin
from django.urls import path, include

from blog.views import (
    inicio,
    formulario_articulos,
    formulario_autores,
    formulario_secciones,
    buscar_articulo,
    buscar_seccion,
    buscar_autor,
)

urlpatterns = [
    path("inicio/", inicio),
    path("formulario-articulos/", formulario_articulos),
    path("formulario-secciones/", formulario_secciones),
    path("formulario-autores/", formulario_autores),
    path("buscar-articulo/", buscar_articulo),
    path("buscar-seccion/", buscar_seccion),
    path("buscar-autor/", buscar_autor),
]
