""" Factory Methods for Tests """

import json
from products.models import Product
from products.serializers import ProductSerializer


def create_test_product(product_code=None):
    """Create a Product and insert it on the database based on the test-product.json file.
    Receives an optinal product_code in case you want to set up the code of the product on the run.
    """
    with open(
        "./products/tests/test-product.json", "r", encoding="UTF-8"
    ) as product_file:
        test_product = json.load(product_file)
        test_product["status"] = Product.Status.IMPORTED
        if product_code:
            test_product["code"] = product_code

    product = ProductSerializer(data=test_product)
    product.is_valid()
    product.save()
    return product.data
