from django import forms
from online.models import Producto, OrdenVenta

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class FormVenta(forms.ModelForm):
    class Meta:
        model = OrdenVenta
        fields = '__all__'

