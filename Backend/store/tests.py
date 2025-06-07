from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Product

User = get_user_model()


class ProductViewsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': 100.00,
            'quantity': 10
        }
        self.list_url = reverse('product-list')  # Make sure to set these names in your urls.py
        self.create_url = reverse('product-create')

    def test_list_products(self):
        # Create some test products
        Product.objects.create(name="Product 1", price=10.00)
        Product.objects.create(name="Product 2", price=20.00)

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming pagination isn't enabled

    def test_create_product(self):
        response = self.client.post(self.create_url, self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Test Product')  