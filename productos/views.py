from rest_framework import viewsets, filters
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Búsqueda y ordenamiento: /api/productos/?search=palabra&ordering=-precio
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "descripcion"]
    ordering_fields = ["precio", "creado", "actualizado", "stock"]
