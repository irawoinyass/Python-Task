from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
# from django.contrib.auth.models import User
from django.test import Client
from accounts.models import User

# Create your tests here.


class TestListCreateCategory(APITestCase):

    def authenticate(self):

        response = self.client.post(reverse(
            "superuser-login"), {"username": "lasisisaheed5@gmail.com", "password": "opeyemi"})

        # self.client.credentials(
        #     HTTP_AUTHORIZATION=f"Token {response.data['token']}")

        # c = Client()

        # response = c.login(
        #     username='lasisisaheed10@gmail.com', password='opeyemi')

        print(response.data)

    def test_create(self):
        self.authenticate()
        # value = {"category_name": "test_name"}
        # response = self.client.post(reverse("create-category"), value)
        # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
