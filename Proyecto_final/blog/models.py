from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=30)
    apodo = models.CharField(max_length=30)
    profecion = models.CharField(max_length=30, blank=True, null=True)
    edad = models.BigIntegerField(blank=True, null=True)
    mail = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.apodo


class Articulo(models.Model):

    titulo = models.CharField(max_length=30)
    articulo = models.CharField(max_length=1000)
    fecha_de_publicacion = models.DateField(null=True)

    def __str__(self):
        return self.titulo


class Seccion(models.Model):
    class Meta:
        verbose_name_plural = "Secciones"

    nombre = models.CharField(max_length=30)
    fecha_de_creacion = models.DateField(null=True)

    def __str__(self):
        return self.nombre
