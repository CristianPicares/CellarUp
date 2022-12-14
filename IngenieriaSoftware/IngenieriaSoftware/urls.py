"""IngenieriaSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from online.views import index, agregarProducto, listaProductos, actualizarProducto, eliminarProducto, codigoQR, agregarOrdenVenta, listaVentas, actualizarOrdenVenta, eliminarOrdenVenta

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('listaProductos/', listaProductos),
    path('agregarProducto/', agregarProducto),
    path('codigoQR/', codigoQR),
    path('login/', codigoQR),
    path('actualizarProducto/<int:id>', actualizarProducto),
    path('eliminarProducto/<int:id>', eliminarProducto),
    path('listaVentas/', listaVentas),
    path('agregarVenta/', agregarOrdenVenta),
    path('actualizarVenta/<int:id>', actualizarOrdenVenta), 
    path('eliminarVenta/<int:id>', eliminarOrdenVenta), 
    ]
