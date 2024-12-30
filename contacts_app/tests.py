from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import Contact

User = get_user_model()

class ContactListTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@gmail.com', password='werte12345')
        self.token = Token.objects.create(user=self.user)
        self.contact = Contact.objects.create(username='Max Mustermann', user=self.user, email="maxmustermann@gmail.com", bgcolor="#FFFFFF", phone="+4934567890")
        self.client = APIClient(enforce_csrf_checks=True)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
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
        self.assertNotEqual(response.data.get('type', None), 'user')
        
    def test_post_contact_list(self):
        url = reverse('contact-list')
        data = {
            'username': 'Cody Mustermann',
            'email': 'codymustermann@gmail.com',
            'phone': '+4934567890',
            'bgcolor': '#FFFFFF',}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 2)
        new_contact = Contact.objects.get(username='Cody Mustermann')
        self.assertEqual(new_contact.email, 'codymustermann@gmail.com')

