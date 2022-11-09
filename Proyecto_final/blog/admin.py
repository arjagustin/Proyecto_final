from django.contrib import admin
from blog.models import Articulo, Autor, Categoria

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Categoria)
admin.site.register(Autor)
