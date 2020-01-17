from .models import usuario, cliente, producto, pago, venta, ventaProducto
from rest_framework import serializers

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('idUsuario', 'cedula', 'nombre', 'apellido', 'telefono', 'edad', 'direccion', 'correo', 'usuario', 'contrasena')

class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('idUsuario', 'cedula', 'nombre', 'apellido', 'telefono', 'edad', 'direccion')

class productoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ('idProducto', 'nombreComercial', 'descripcion', 'precio', 'cantidadDisponible', 'esMedicamento', 'url', 'estado')

class pagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pago
        fields = ('idPago', 'fechaHora')

class ventaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('idVenta','total','factura', 'idCliente', 'idUsuario','idPago')

class ventaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventaProducto
        fields = ('idVentaProducto','cantidad','idProducto', 'idVenta')