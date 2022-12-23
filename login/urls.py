from django.urls import path
from .views import exit,register

urlpatterns = [
    
    path('logout/', exit, name='exit'),

]