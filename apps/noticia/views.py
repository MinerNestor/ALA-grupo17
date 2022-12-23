from django.shortcuts import render
from apps.noticia.models import Noticia
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Noticia
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Noticia, Categoria 
from apps.comentario.models import Comentarios
from apps.comentario.forms import ComentarioForm
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.





#----------------
class NoticiaListview(ListView):
    model = Noticia
    template_name = 'noticia/listadoNoticias.html'


def noticias(request):
    return render(request, 'noticia/listadoNoticias.html')



class CategoriaListview(ListView):
    model = Categoria
    template_name = 'noticia/categorias.html'


class AgregarNoticia(LoginRequiredMixin, CreateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/AgregarNoticia.html'
    success_url   = reverse_lazy('apps.noticia:noticias')


class AgregarCategoria(LoginRequiredMixin,CreateView):
    model         = Categoria
    fields        = ['nombre', 'id']
    template_name = 'noticia/AgregarCategoria.html'
    success_url   = reverse_lazy('apps.noticia:AgregarNoticia')


class ActualizarNoticia(LoginRequiredMixin,UpdateView):
    model         = Noticia
    fields        = ['titulo', 'subtitulo','texto','categoria','imagen']
    template_name = 'noticia/AgregarNoticia.html'
    success_url   = reverse_lazy('apps.noticia:noticias')

class BorrarNoticia(LoginRequiredMixin,DeleteView):
    model           = Noticia
    template_name = 'noticia/borrarnoticia.html'
    success_url   = reverse_lazy('apps.noticia:noticias')
class BorrarCategoria(LoginRequiredMixin,DeleteView):
    model           = Categoria
    template_name = 'noticia/borrarcategoria.html'
    success_url   = reverse_lazy('apps.noticia:noticias')


def listarporcategoria(request, categoria):
    categoria2 = Categoria.objects.filter(nombre=categoria)
    noticia    = Noticia.objects.filter(categoria=categoria2[0].id)
    categorias  = Categoria.objects.all()
    context    = {
        'noticia' : noticia,
        'categoria': categorias,
    }
    return render(request,'noticia/listarporcategoria.html',context)


def ExistePost(id):
    for i in Noticia:
        if i.id == id:
            return i
    return None

def LeerPost(request, id):
    try:
        posts   = ExistePost(id)
    except Exception:
        posts   = Noticia.objects.get(id=id)
        comentarios = Comentarios.objects.filter(noticia=id)

    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            aux         =  form.save(commit=False)
            aux.noticia = posts
            aux.usuario = request.user
            aux.save()
            form        = ComentarioForm()
        else:
            return redirect('usuario:login')

    context = {
        'titulo': 'noticia',
        'posts': posts,
        'form': form,
        'comentarios': comentarios,
    }
    return render(request,'noticia/post.html', context)
