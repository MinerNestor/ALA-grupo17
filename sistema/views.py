from django.shortcuts import render,redirect
from apps.noticia.models import Noticia
from django.views.generic import ListView
from .views import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

class NoticiaListview(ListView):
    model = Noticia
    template_name = 'noticia/listadoNoticias.html'



def inicio(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'about.html')

def noticias(request):
    return render(request, 'noticia/listadoNoticias.html')



def exit(request):
    logout(request)
    return redirect('inicio')


def register(request):
  data = {
      'form': UserCreationForm()
  }
  if request.method == 'POST':
      user_creation_form = UserCreationForm(data=request.POST)
      if user_creation_form.is_valid():
          user_creation_form.save()
          user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
          login(request, user)
          return redirect('index')
  
  return render(request, 'registration/register.html', data)



