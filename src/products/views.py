""" Products Django App Views """

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class GetProductByCode(generics.RetrieveAPIView):
    """Get a product by code"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "code"


class ListProducts(generics.ListAPIView):
    """List all the products by page"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
