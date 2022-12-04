from django.shortcuts import render
from online.models import Producto
from online.forms import FormProducto
from . import forms
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def agregarProducto(request):
    form = forms.FormProducto()
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            form.save()
        return listaProductos(request)
    data = {'form' : form,
            'titulo':'AGREGAR PRODUCTO',
             'boton':'AGREGAR PRODUCTO'}
    return render(request, 'agregarProducto.html', data)

def listaProductos(request):
    producto = Producto.objects.all()
    data = {'producto':producto}
    return render(request, 'listaProductos.html', data)

def actualizarProducto(request, id):
    producto = Producto.objects.get(idProducto = id)
    form = FormProducto(instance=producto)
    print(request.method+' '+str(id))
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('../listaProductos/')
    datos = {'form':form,
             'titulo':'ACTUALIZAR PRODUCTO',
             'boton':'ACTUALIZAR PRODUCTO'}
    return render(request,'agregarProducto.html',datos)

def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete()
    return listaProductos(request)