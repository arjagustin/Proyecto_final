from django.contrib import admin
from django.urls import path, include

from blog.views import (
    inicio,
    formulario_articulos,
    formulario_autores,
    formulario_secciones,
)

urlpatterns = [
    path("inicio/", inicio),
    path("formulario-articulos/", formulario_articulos),
    path("formulario-secciones/", formulario_secciones),
    path("formulario-autores/", formulario_autores),
]
