from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

#! Es necesario este nombre, para ser llamado desde la plantilla, por ejemplo: {% url 'home:index' %}
app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
] + staticfiles_urlpatterns()
