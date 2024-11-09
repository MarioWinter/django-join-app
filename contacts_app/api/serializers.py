from rest_framework import serializers
from django.contrib.auth.models import User

from contacts_app.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    #zum Testen
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'bgcolor', 'user']
