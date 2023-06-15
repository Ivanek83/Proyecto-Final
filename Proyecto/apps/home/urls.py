from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

#! Es necesario este nombre, para ser llamado desde la plantilla, por ejemplo: {% url 'home:index' %}
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('planes/', views.planes, name='planes'),
    path('tu_info/', views.tu_info, name='tu_info'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('cargar_datos/', views.cargar_datos, name='cargar_datos'),
    path('editar_datos/', views.editar_datos, name='editar_datos'),
    path('subir_archivo/', views.subir_archivo, name='subir_archivo'),
] + staticfiles_urlpatterns()
