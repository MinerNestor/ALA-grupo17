
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from django.views.generic import DeleteView
from apps.usuario.models import Usuario
from django.urls import reverse_lazy
# Create your views here.



def Comentar(request):
    comentarios = Comentarios.objects.all()
    usuario = request.user.id

    context={
        'comentarios' : comentarios,
        'usuario': usuario,
    }
    return render(request,'comentario/listadoComentario.html', context)


def agregarComentario(request):
    usuario = Usuario(usuario = request.user)
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ComentarioForm()


    context={
        'form': form,
        'usuario': usuario,
    }
    return render(request,'comentario/agregarComentario.html', context)


class DeleteComentario(DeleteView):
    model = Comentarios
    template_name = 'comentario/eliminarComentario.html'
    success_url = reverse_lazy('apps.noticia:noticias')