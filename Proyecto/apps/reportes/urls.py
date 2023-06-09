from django.urls import path
from . import views

#! Es necesario este nombre, para ser llamado desde la plantilla, por ejemplo: {% url 'reportes:index' %}
#app_name = 'reportes'

urlpatterns = [
    path('', views.index, name='index'),
]
