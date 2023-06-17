""" Django Products App Configuration """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Configuration for Products App"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
