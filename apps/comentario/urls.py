
from django.urls import path
from . import views

app_name = 'apps.comentario'

urlpatterns = [
    path('agregarComentario/', views.agregarComentario,name="agregarComentario"),
    path('comentar/', views.Comentar, name="comentar"),
    path('eliminarComentario/<pk>', views.DeleteComentario.as_view(),name="eliminarComentario"),
]