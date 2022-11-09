from django.db import models

# Create your models here.


class Autor(models.Model):
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=30)
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.user


class Articulo(models.Model):

    titulo = models.CharField(max_length=30)
    articulo = models.CharField(max_length=1000)
    fecha_de_publicacion = models.DateField(null=True)

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    class Meta:
        verbose_name_plural = "categorías"

    Categorias = models.CharField(max_length=30)

    def __str__(self):
        return self.Categorias
