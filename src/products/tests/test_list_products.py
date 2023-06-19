# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from rest_framework.test import APIClient, APITestCase
from .factories import create_test_product


class TestListProducts(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_no_products(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data["results"]), 0)

    def test_success(self):
        product = create_test_product()

        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

        self.assertEqual(response.data["results"][0]["code"], str(product["code"]))

    def test_pagination_size(self):
        product = create_test_product()

        create_test_product(3661112502850123)

        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

        self.assertEqual(response.data["results"][0]["code"], str(product["code"]))
