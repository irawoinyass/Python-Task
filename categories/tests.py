from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class TestListCreateCategory(APITestCase):

    def authenticate(self):
        response = self.client.post(reverse(
            "superuser-login"), {"username": "lasisisaheed10@gmail.com", "password": "opeyemi"})

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Token {response.data['token']}")

    def create_test(self):
        # self.authenticate()
        value = {"category_name": "test_name"}
        response = self.client.post(reverse("create-category"), value)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
