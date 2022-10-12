from django.db import models

# Create your models here.


class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    mail = models.EmailField


class articulo(models.Model):
    titulo = models.CharField(max_length=30)
    articulo = models.CharField(max_length=1000)
    fecha_de_publicacion = models.DateField(none=True)


class seccion(models.Model):
    nombre = models.CharField(max_length=30)
