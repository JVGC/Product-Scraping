# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from rest_framework.test import APIClient, APITestCase
from rest_framework.exceptions import NotFound
from products.models import Product


class TestGetProductByCode(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_product_exist(self):
        product_code = 3661112502850
        product = Product.objects.create(
            code=3661112502850,
            barcode="3661112502850(EAN / EAN-13)",
            status=Product.Status.IMPORTED,
            imported_t="2020-02-07T16:00:00Z",
            url="https://world.openfoodfacts.org/product/3661112502850",
            product_name="Jambon de Paris cuit à l'étouffée",
            quantity="240 g",
            categories="Meats, Prepared meats, Hams, White hams",
            packaging="Film en plastique, Film en plastique",
            brands="Tradilège, Marque Repère",
            image_url="https://static.openfoodfacts.org/images/products/366/111/250/2850/front_fr.3.400.jpg",
        )

        product.save()

        response = self.client.get(f"/products/{product_code}")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["code"], str(product_code))

    def test_product_does_not_exist(self):
        response = self.client.get("/products/123")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"].code, NotFound.default_code)
