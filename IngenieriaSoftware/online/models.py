from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=50)
    colorProducto = models.CharField(max_length=20)
    dimesionesProducto = models.CharField(max_length=15)
    pesoProducto = models.CharField(max_length=6)
    marcaProducto = models.CharField(max_length=6)