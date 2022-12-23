from django.db import models
from django.utils import timezone
from django.contrib.auth.models import *
from django.urls import reverse
from datetime import datetime, date


# Create your models here.


# --- Noticia
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        #return reverse(detalle de articulo)
        return reverse('inicio')

class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticia', default='noticia/default.png')
    publicado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

    def delete(self, using = None, keep_parents = False):
        self.imagen.delete(self.imagen.name)
        super().delete()










