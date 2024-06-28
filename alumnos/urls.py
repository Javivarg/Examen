from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    #path('crud', views.crud, name='crud'),
    path('productos', views.productos, name='productos'),
    path('inicioS', views.inicioS, name='inicioS'),
    path('crearU', views.crearU, name='crearU'),
]