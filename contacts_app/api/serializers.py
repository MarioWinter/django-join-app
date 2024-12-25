from rest_framework import serializers
from django.contrib.auth import get_user_model
from contacts_app.models import Contact
from drf_spectacular.utils import extend_schema_field
User = get_user_model()


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.
    This serializer handles the serialization and deserialization of Contact instances,
    including custom validation for the email field and a method to determine the type
    of contact.
    Attributes:
        type (SerializerMethodField): A custom field to determine the type of contact.
        user (PrimaryKeyRelatedField): A field to associate the contact with a user.
    Methods:
        validate_email(value):
            Validates that the email address is unique for the user.
            Args:
                value (str): The email address to validate.
            Returns:
                str: The validated email address.
            Raises:
                serializers.ValidationError: If the email address already exists for the user.
        get_type(obj):
            Determines the type of contact based on the user's email and username.
            Args:
                obj (Contact): The contact instance.
            Returns:
                str: "user" if the contact's email and username match the user's, otherwise "contact".
    """
    type = serializers.SerializerMethodField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Contact
        fields = ['id', 'username', 'email', 'phone', 'bgcolor', 'user', 'type']

    def validate_email(self, value):
        user = self.context['request'].user
        if self.instance is None:
            if Contact.objects.filter(user=user, email=value).exists():
                raise serializers.ValidationError("This email address already exists.")
        else:
            if Contact.objects.filter(user=user, email=value).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("This email address already exists.")
        return value

    @extend_schema_field(str)
    def get_type(self, obj) -> str:
    
        if obj.user.email == obj.email and obj.user.username == obj.username:
            return "user"
        
        return "contact"
