# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from rest_framework.test import APIClient, APITestCase
from products.models import Product


class TestListProducts(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_no_products(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data["results"]), 0)

    def test_success(self):
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

        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

        self.assertEqual(response.data["results"][0]["code"], str(product_code))

    def test_pagination_size(self):
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

        product2 = Product.objects.create(
            code=36611125028501,
            barcode="36611125028501(EAN / EAN-13)",
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

        product2.save()

        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)

        self.assertEqual(response.data["results"][0]["code"], str(product_code))
