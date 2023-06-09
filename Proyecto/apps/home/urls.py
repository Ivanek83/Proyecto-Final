from django.urls import path
from . import views

#! Es necesario este nombre, para ser llamado desde la plantilla, por ejemplo: {% url 'home:index' %}
#app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
]
