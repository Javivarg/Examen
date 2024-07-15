from django.shortcuts import render, redirect
from .models import Categoria, Producto
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def index(request):
    productos = Producto.objects.all()
    context = {"productos": productos}
    return render(request, 'alumnos/index.html', context)

def carrito(request):
    context = {}
    return render(request, 'alumnos/carrito.html', context)

def registro(request):
    context = {}
    return render(request, 'alumnos/carro.html', context)


def plantas(request):
    plantas=Producto.objects.raw('SELECT * FROM alumnos_producto WHERE idCategoria = 1')
    context={ "plantas":plantas,}
    return render(request, 'alumnos/plantas.html', context)

def maceteros(request):
    maceteros=Producto.objects.raw('SELECT * FROM alumnos_producto WHERE idCategoria = 2')
    context={ "maceteros":maceteros}
    return render(request, 'alumnos/maceteros.html', context)

def tierras(request):
    tierras=Producto.objects.raw('SELECT * FROM alumnos_producto WHERE idCategoria = 3')
    context={ "tierras":tierras}
    return render(request, 'alumnos/tierras.html', context)

def crud(request):
    productos = Producto.objects.all
    categoria = Categoria.objects.all
    context={"productos": productos, "categoria":categoria}
    return render(request, 'alumnos/productos_list.html', context)


def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)
        producto.delete()
        mensaje="Producto eliminado"
        productos=Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'alumnos/productos_list.html', context)
    except:
        mensaje='Error Producto no Existe'
        productos=Producto.objects.all()
        context={'productos':productos,'mensaje':mensaje}
        return render(request, 'alumnos/productos_list.html', context)
    
def productos_findEdit(request, pk):
    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        categorias=Categoria.objects.all()

        context={"producto": producto, "categoria":categorias}
        if producto:
            return render(request,'alumnos/productos_edit.html',context)
        else:
            context={'mensaje':"Error producto no existe"}
            return render(request, 'alumnos/productos_list.html', context)
        
def productosAdd(request):
    if request.method != "POST":
        categorias=Categoria.objects.all()
        context={"categorias":categorias}
        return render(request, 'alumnos/productosAdd.html', context)
    else:
        id_producto=request.POST["idProducto"]
        producto=request.POST["producto"]
        precio=request.POST["precio"]
        categoria=request.POST["categoria"]
        activo="1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)
        obj=Producto.objects.create(
            id_producto=id_producto,
            producto=producto,
            precio=precio,
            id_categoria=objCategoria,
            activo=1
        )
        obj.save()
        context={'mensaje':"OK, Producto guardado"}
        return render(request,'alumnos/productosAdd.html',context)
        
def productosUpdate(request):
    if request.method == "POST":
        id_producto=request.POST["idProducto"]
        producto=request.POST["producto"]
        precio=request.POST["precio"]
        categoria=request.POST["categoria"]
        activo="1"

        objCategoria=Categoria.objects.get(id_categoria = categoria)

        producto=Producto()
        producto.id_producto=id_producto
        producto.producto=producto
        producto.precio=precio
        producto.id_categoria=objCategoria
        producto.activo=1
        producto.save()

        categorias=Categoria.objects.all()
        context={'Mensaje':"OK, datos actualizados", 'categorias':categorias, 'producto':producto}
        return render(request, 'alumnos/productos_edit.html', context)
    else:
        productos=Producto.objects.all()
        context={'productos':productos}
        return render(request, 'alumnos/productos_list.html', context)
    
class VistaRegistro(View):

    #noinspecton PyMethodMayBeStatic
    def get(self, request):
        form = UserCreationForm()
        return render(request,'alumnos/registro.html',{"form":form})
    
    #noinspecton PyMethodMayBeStatic
    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, F"Bienvenido a la pagina {nombre}")
            login(request, usuario)
            return redirect("index")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

def acceder(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, F"Bienvenido a la pagina {nombre}")
                return redirect("index")
            else:
                messages.error(request, "los datos son incorrectos")
        else:
            messages.error(request, "los datos son incorrectos")
    form=AuthenticationForm()
    return render(request, 'alumnos/login.html', {'form':form})

def salir(request):
    logout(request)
    messages.success(request, "Secion cerrada correctamente")
    return redirect("index")


