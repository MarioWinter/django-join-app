from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class ContactListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='werte12345')
        self.client.force_authenticate(user=self.user)
    
    def test_get_contacts(self):
        url = reverse('contact-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
