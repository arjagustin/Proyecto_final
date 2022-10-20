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
    path("inicio/formulario-articulo.html/", formulario_articulos),
    path("inicio/formulario-seccion.html/", formulario_secciones),
    path("inicio/formulario-autor.html/", formulario_autores),
    path("inicio/formulario-busqueda-articulo.html/", buscar_articulo),
    path("inicio/formulario-busqueda-seccion.html/", buscar_seccion),
    path("inicio/formulario-busqueda-autor.html/", buscar_autor),
]
