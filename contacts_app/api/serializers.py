from rest_framework import serializers
from django.contrib.auth import get_user_model
from contacts_app.models import Contact
User = get_user_model()

class ContactSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'phone', 'bgcolor', 'user']
        
    def validate_email(self, value):
        user = self.context['request'].user
        if Contact.objects.filter(user=user, email=value).exists():
            raise serializers.ValidationError("This E-mail address already exists")
        return value