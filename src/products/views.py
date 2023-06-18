""" Habits Django App Views """

from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class GetProductByCode(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "code"


class ListProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
