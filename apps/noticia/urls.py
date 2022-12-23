"""paginablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import NoticiaListview, noticias,  CategoriaListview
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'apps.noticia'


urlpatterns = [
    path('noticias/', noticias((NoticiaListview))),   
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from .views import NoticiaListview




urlpatterns = [
    path("noticias", NoticiaListview.as_view(), name='noticias'),
    path("categorias", CategoriaListview.as_view(), name='categorias'),
    path('listarporcategoria/<str:categoria>',views.listarporcategoria, name='listarporcategoria'),
    path('AgregarNoticia/', views.AgregarNoticia.as_view(),name="AgregarNoticia"),
    path('AgregarCategoria/', views.AgregarCategoria.as_view(),name="AgregarCategoria"),
    path('BorrarCategoria/<pk>', views.BorrarCategoria.as_view(),name="BorrarCategoria"),
    path('Leerpost/<int:id>', views.LeerPost, name="Leerpost"),
    path('BorrarNoticia/<pk>', views.BorrarNoticia.as_view(),name="BorrarNoticia"),
    path('ActualizarNoticia/<pk>', views.ActualizarNoticia.as_view(), name="ActualizarNoticia"), 
]