""" Scraper Pipelines """
from datetime import datetime
from asgiref.sync import sync_to_async

from products.models import Product


class DjangoPipeline:
    """
    Saves Item to the database
    """

    @sync_to_async
    def process_item(self, item, _):
        """Add Scrapped product to Database"""
        item["imported_t"] = datetime.utcnow().isoformat() + "Z"
        item["status"] = Product.Status.IMPORTED
        item.save()
        return item
