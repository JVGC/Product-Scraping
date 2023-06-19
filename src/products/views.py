""" Products Django App Views """

from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer


@extend_schema(tags=["Products"])
class GetProductByCode(generics.RetrieveAPIView):
    """Get a product by code"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "code"


@extend_schema(tags=["Products"])
class ListProducts(generics.ListAPIView):
    """List all the products by page"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
