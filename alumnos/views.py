from django.shortcuts import render
from .models import Categoria, Producto
# Create your views here.

def index(request):
    context = {}
    return render(request, 'alumnos/index.html', context)


def productos(request):
    productos = Producto.objects.all  # Filtra solo productos activos
    context={"productos": productos}
    return render(request, 'alumnos/productos.html', context)

def inicioS(request):
    context = {}
    return render(request, 'alumnos/inicioS.html', context)

def crearU(request):
    context = {}
    return render(request, 'alumnos/crearU.html', context)


#def crud(request):
#    alumnos = Alumno.objects.all()
#    context = {'alumnos':alumnos}
#    return render(request, 'alumnos/alumnos_list.html', context)
