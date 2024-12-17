from rest_framework import serializers
from django.contrib.auth import get_user_model
from contacts_app.models import Contact
from user_auth_app.api.serializers import CustomUserSerializer
User = get_user_model()


class ContactSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())
    class Meta:
        model = Contact
        fields = ['id', 'username', 'email', 'phone', 'bgcolor', 'user', 'type']
        
    def validate_email(self, value):
        user = self.context['request'].user
        if value == user.email:
            raise serializers.ValidationError("You cannot add your own email address as a contact.")
        
        
        if Contact.objects.filter(user=user, email=value).exists():
            raise serializers.ValidationError("This email address already exists.")
        return value

    def get_type(self, obj):
        return 'contact'

class ContactUserListSerializer(serializers.Serializer):
    def to_representation(self, instance):
        user_serializer = CustomUserSerializer(instance['user'])
        contacts_serializer = ContactSerializer(instance['contacts'], many=True)
        return [user_serializer.data] + contacts_serializer.data