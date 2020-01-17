from django.contrib import admin
from .models import usuario, cliente, producto, pago, venta, ventaProducto

# Register your models here.

myModels = [usuario, cliente, producto, pago, venta, ventaProducto]  # iterable list
admin.site.register(myModels)
