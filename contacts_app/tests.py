from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from .models import Contact

User = get_user_model()

class ContactListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='werte12345')
        self.client.force_authenticate(user=self.user)
        self.contact = Contact.objects.create(username='Max Mustermann', user=self.user, email="maxmustermann@gmail.com", bgcolor="#FFFFFF", phone="+4934567890")
    
    def test_get_contacts_list(self):
        url = reverse('contact-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_contact_detail(self):
        url = reverse('contact-detail', kwargs={'pk': self.contact.id})
        response = self.client.get(url)
        expected_data = {
            'id': self.contact.id,
            'username': 'Max Mustermann',
            'email': 'maxmustermann@gmail.com',
            'phone': '+4934567890',
            'bgcolor': '#FFFFFF',
            'user': self.user.id,
            'type': 'contact'}
        #print("Response data:", response.data)
        #print("Expected data:", expected_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
