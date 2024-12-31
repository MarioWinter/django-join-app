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
      
        
    def test_create_contact_list(self):
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
    
    
    def test_update_contact_detail(self):
        url = reverse('contact-detail', kwargs={'pk': self.contact.id})
        data = {
            'username': 'Maxi Mustermann',
            'email': 'maximustermann@gmail.com',
            'phone': '+4934567890',
            'bgcolor': '#FFFFFF',
            'user': self.user.id,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().username, 'Maxi Mustermann')
        self.assertEqual(Contact.objects.get().email, 'maximustermann@gmail.com')
        
        
    def test_patch_contact_detail(self):
        url = reverse('contact-detail', kwargs={'pk': self.contact.id})
        data = {
            'username': 'Mario Mustermann',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().username, 'Mario Mustermann')

    
    #unauthorized user 
    def test_create_contact_list_unauthorized(self):
        """
        Tests whether the creation of a contact fails when the CSRF token is missing.
        """
        csrf_client = APIClient(enforce_csrf_checks=True)
        url = reverse('contact-list')
        data = {
            'username': 'unauthorized contact',
            'email': 'unauthorized@gmail.com',
            'phone': '+1234567890',
            'bgcolor': '#FFFFFF',}
        response = csrf_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


