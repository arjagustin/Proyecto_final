from socket import fromshare
from django import forms


class Articuloform(forms.Form):

    titulo = forms.CharField(max_length=30)
    articulo = forms.CharField(max_length=1000)
    fecha_de_publicacion = forms.DateField()


class Autorform(forms.Form):
    nombre = forms.CharField(max_length=30)
    apodo = forms.CharField(max_length=30)
    profecion = forms.CharField(max_length=30)
    edad = forms.IntegerField()
    mail = forms.EmailField()


class Categoriaform(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_de_creacion = forms.DateField()
