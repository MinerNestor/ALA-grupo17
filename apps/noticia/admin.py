from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)

@admin.register(Noticia)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id','activo', 'fecha', 'categoria')
  
    



