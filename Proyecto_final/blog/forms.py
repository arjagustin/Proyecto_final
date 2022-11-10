from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class Registrousuario(UserCreationForm):
    user = forms.CharField()
    mail = forms.EmailField()
    password1 = forms.CharField(label='Contraseña' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email',
#                                                           'class': "controls"}))
#    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput
#                                (attrs={'placeholder': 'Contraseña', 'class': "controls"})
#                                )
#    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput
#                                (attrs={'placeholder': 'Ingrese contraseña de nuevo',
#                                        'class': "controls"})
#                                )
    