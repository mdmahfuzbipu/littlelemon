from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('menu-items')
        
        self.user = User.objects.create_user(username="testuser", password="testtest456")
        self.token = Token.objects.create(user=self.user)
        
        self.client.credentials(HTTP_AUTHORIZATION = 'Token ' + self.token.key)
        
        MenuItem.objects.create(title="Burger", price=250, inventory = 10)
        MenuItem.objects.create(title="Salad", price=250, inventory = 10)
        
        
    def test_get_all(self):
        
        response = self.client.get(self.url)
        
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
        