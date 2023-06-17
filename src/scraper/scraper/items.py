from scrapy_djangoitem import DjangoItem
from products.models import Product


class ScraperItem(DjangoItem):
    django_model = Product
