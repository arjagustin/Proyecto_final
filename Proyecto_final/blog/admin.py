from django.contrib import admin
from blog.models import articulo, usuario, seccion

# Register your models here.

admin.site.register(articulo)
admin.site.register(seccion)
admin.site.register(usuario)
