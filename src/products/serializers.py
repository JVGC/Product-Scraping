""" Product Serializers """
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product Serializer. All the fields in the model are returned"""

    class Meta:
        model = Product
        lookup_field = "code"
        fields = "__all__"
