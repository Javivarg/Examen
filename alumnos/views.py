from django.shortcuts import render
from .models import Categoria, Producto
# Create your views here.

def index(request):
    context = {}
    return render(request, 'alumnos/index.html', context)


def productos(request):
    productos = Producto.objects.all
    context={"productos": productos}
    return render(request, 'alumnos/productos.html', context)

def inicioS(request):
    context = {}
    return render(request, 'alumnos/inicioS.html', context)

def crearU(request):
    context = {}
    return render(request, 'alumnos/crearU.html', context)


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
        #ERROR AQUIIIII

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

        objCategoria=Categoria.objects.get(id_categoria = categoria)

        productos=Producto()
        productos.id_producto=id_producto
        productos.producto=producto
        productos.precio=precio
        productos.id_categoria=objCategoria
        productos.save()

        categorias=Categoria.objects.all()
        context={'Mensaje':"OK, datos actualizados", 'categorias':categorias, 'productos':productos}
        return render(request, 'alumnos/productos_list.html', context)
    else:
        productos=Producto.objects.all()
        context={'productos':productos}
        return render(request, 'alumnos/productos_list.html', context)
