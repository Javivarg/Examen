from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'producto', 'precio', 'activo', 'idCategoria', 'imagen']