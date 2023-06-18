from rest_framework.test import APIClient, APITestCase


class TestHome(APITestCase):
    def test_home_string_return(
        self,
    ):
        client = APIClient()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Fullstack Challenge 20201026")
