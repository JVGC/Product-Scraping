from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

x = [
    {
        "imported_t": "2020-02-07T16:00:00Z",
    }
]


class Product(models.Model):
    code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    url = models.URLField()
    image_url = models.URLField()
    barcode = models.CharField(max_length=100)
    brands = models.CharField(max_length=100)
    packaging = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)

    imported_t = models.DateTimeField(verbose_name="imported_time")

    class Status(models.TextChoices):
        DRAFTED = "DR", _("Drafted")
        IMPORTED = "IM", _("Imported")

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.IMPORTED
    )
