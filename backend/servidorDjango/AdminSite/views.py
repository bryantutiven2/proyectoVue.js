from django.http import HttpResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import usuario, cliente, producto, pago, venta, ventaProducto
from .serializers import usuarioSerializer, clienteSerializer, productoSerializer, pagoSerializer, ventaSerializer, ventaProductoSerializer

# Create your views Usuarios

class UsuariosList(APIView):
    def get(self, request, format=None):
        usuarios1 = usuario.objects.all()
        serializer = usuarioSerializer(usuarios1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = usuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuariosDetalle(APIView):

    def get_object(self, pk):
        try:
            return usuario.objects.get(usuario=pk)
        except usuario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        serializer = usuarioSerializer(usuarios1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        serializer = usuarioSerializer(usuarios1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuarios1 = self.get_object(pk)
        usuarios1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Clientes

class ClientesList(APIView):
    def get(self, request, format=None):
        cliente1 = cliente.objects.all()
        serializer = clienteSerializer(cliente1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = clienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientesDetalle(APIView):

    def get_object(self, pk):
        try:
            return cliente.objects.get(usuario=pk)
        except cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente1 = self.get_object(pk)
        serializer = clienteSerializer(cliente1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cliente1 = self.get_object(pk)
        serializer = clienteSerializer(cliente1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente1 = self.get_object(pk)
        cliente1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Producto

class ProductosList(APIView):
    def get(self, request, format=None):
        producto1 = producto.objects.all()
        serializer = productoSerializer(producto1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = productoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductosDetalle(APIView):

    def get_object(self, pk):
        try:
            return producto.objects.get(idProducto=pk)
        except producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto1 = self.get_object(pk)
        serializer = productoSerializer(producto1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        producto1 = self.get_object(pk)
        serializer = productoSerializer(producto1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto1 = self.get_object(pk)
        producto1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Pago

class PagoList(APIView):
    def get(self, request, format=None):
        pago1 = pago.objects.all()
        serializer = pagoSerializer(pago1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = pagoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PagoDetalle(APIView):

    def get_object(self, pk):
        try:
            return pago.objects.get(id=pk)
        except pago.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pago1 = self.get_object(pk)
        serializer = pagoSerializer(pago1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pago1 = self.get_object(pk)
        serializer = pagoSerializer(pago1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pago1 = self.get_object(pk)
        pago1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views Ventas

class VentaList(APIView):
    def get(self, request, format=None):
        venta1 = venta.objects.all()
        serializer = ventaSerializer(venta1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ventaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VentaDetalle(APIView):

    def get_object(self, pk):
        try:
            return venta.objects.get(pk=pk)
        except venta.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        venta1 = self.get_object(pk)
        serializer = ventaSerializer(venta1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        venta1 = self.get_object(pk)
        serializer = ventaSerializer(venta1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        venta1 = self.get_object(pk)
        venta1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views VentaProducto

class VentaProductoList(APIView):
    def get(self, request, format=None):
        ventaProducto1 = ventaProducto.objects.all()
        serializer = ventaProductoSerializer(ventaProducto1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ventaProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VentaProductoDetalle(APIView):

    def get_object(self, pk):
        try:
            return ventaProducto.objects.get(pk=pk)
        except ventaProducto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ventaProducto1 = self.get_object(pk)
        serializer = ventaProductoSerializer(ventaProducto1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        ventaProducto1 = self.get_object(pk)
        serializer = ventaProductoSerializer(ventaProducto1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ventaProducto1 = self.get_object(pk)
        ventaProducto1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)