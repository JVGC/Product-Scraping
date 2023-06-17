"""Product Scraper Items"""
from scrapy_djangoitem import DjangoItem
from products.models import Product


class ProductItem(DjangoItem):
    """Product Django Item for Scrapy"""

    django_model = Product
