""" Django Product Model """
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """Django Product Model"""

    code = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=200)
    url = models.URLField()
    image_url = models.URLField()
    barcode = models.CharField(max_length=100)
    brands = models.CharField(max_length=300)
    packaging = models.CharField(max_length=500)
    quantity = models.CharField(max_length=50)
    categories = models.CharField(max_length=500)

    imported_t = models.DateTimeField(verbose_name="imported_time")

    class Status(models.TextChoices):
        """Product Status Enum"""

        DRAFTED = "DR", _("Drafted")
        IMPORTED = "IM", _("Imported")

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.IMPORTED
    )

    class Meta:
        ordering = ["imported_t"]
