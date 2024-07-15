from django.urls import path
from . import views
from .views import VistaRegistro

urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', VistaRegistro.as_view(), name='registro'),
    path('login', views.acceder, name='login'),
    path('salir', views.salir, name='salir'),
    path('acceder', views.acceder, name='acceder'),
    path('plantas', views.plantas, name='plantas'),
    path('maceteros', views.maceteros, name='maceteros'),
    path('tierras', views.tierras, name='tierras'),
    path('carrito', views.carrito, name='carrito'),

    path('crud', views.crud, name='crud'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', views.productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', views.productosUpdate, name='productosUpdate'),  
]