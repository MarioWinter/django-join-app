from rest_framework import serializers
from django.contrib.auth.models import User

from contacts_app.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'bgcolor']
