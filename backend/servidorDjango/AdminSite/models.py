from django.db import models

# Create your models here.
class usuario(models.Model):
    idUsuario = models.AutoField (primary_key = True, unique=True)
    cedula = models.CharField (max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=20)
    correo = models.EmailField(max_length=200)
    usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=20)

class cliente(models.Model):
    idCliente = models.AutoField(primary_key=True, unique=True)
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)

class pago(models.Model):
    idPago = models.AutoField(primary_key=True, unique=True)
    fechaHora = models.DateTimeField()

class producto(models.Model):
    idProducto = models.AutoField(primary_key=True, unique=True)
    nombreComercial = models.CharField(max_length=300)
    descripcion = models.TextField()
    precio = models.FloatField(null=True, blank=True, default=None)
    cantidadDisponible = models.IntegerField()
    esMedicamento = models.BooleanField(default=False)
    url = models.CharField(max_length=800)
    estado = models.BooleanField(default=True)

class venta(models.Model):
    idVenta = models.AutoField(primary_key=True, unique=True)
    total = models.FloatField(null=True, blank=True, default=None)
    factura = models.CharField(max_length=100)
    idCliente =  models.ForeignKey(cliente, on_delete=models.PROTECT, null=True, default=None)
    idUsuario = models.ForeignKey(usuario, on_delete=models.PROTECT)
    idPago = models.ForeignKey(pago, on_delete=models.PROTECT)

class ventaProducto(models.Model):
    idVentaProducto = models.AutoField(primary_key=True, unique=True)
    cantidad = models.IntegerField()
    idProducto = models.ForeignKey(producto, on_delete=models.PROTECT)
    idVenta = models.ForeignKey(venta, on_delete=models.PROTECT)