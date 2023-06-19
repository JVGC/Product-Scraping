# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from rest_framework.test import APIClient, APITestCase
from rest_framework.exceptions import NotFound
from .factories import create_test_product


class TestGetProductByCode(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_product_exist(self):
        product = create_test_product()

        response = self.client.get(f"/products/{product['code']}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["code"], str(product["code"]))

    def test_product_does_not_exist(self):
        response = self.client.get("/products/123")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"].code, NotFound.default_code)
