from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView

#from .views import
app_name = 'apps.usuario'

urlpatterns = [
    path('registrar/', views.RegistrarUsuario.as_view(), name="registrar"),
    path('login/', LoginView.as_view(template_name="usuario/login.html"),name="login"),
    path('logout/', LogoutView.as_view(template_name="usuario/logout.html"),name="logout"),
    path('listarUsuarios/', views.Usuario,name="listarUsuarios"),
    path('deleteUsuario/<pk>', views.DeleteUsuario.as_view(),name="eliminarUsuario"),
    path('reset/password_reset', PasswordResetView.as_view(), {'template_name':'password/password_reset_form.html', 'email_template_name': 'password/password_reset_email.html'}, name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(), {'template_name':'password/password_reset_done.html'}, name='password_reset_done'),
    path('reset/password_reset_complet', PasswordResetCompleteView.as_view(), {'template_name':'password/password_reset_complete.html'}, name='password_reset_complete'),
]
