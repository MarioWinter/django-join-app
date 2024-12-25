from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from user_auth_app.api.utils import generate_random_color
User = get_user_model()



class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    This serializer handles user registration by validating the input data,
    including password confirmation and email uniqueness. It also generates
    a random background color for the user.
    Attributes:
        repeated_password (serializers.CharField): Field for confirming the password.
    Meta:
        model (User): The user model to be serialized.
        fields (list): List of fields to be included in the serialization.
        extra_kwargs (dict): Additional keyword arguments for the fields.
    Methods:
        save(): Validates the input data, checks for password match and email uniqueness,
                creates a new user with the provided data, and returns the created user instance.
    """
    
    repeated_password = serializers.CharField(write_only=True)
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
                
    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        email = self.validated_data['email']
        username = self.validated_data['username']
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'password-error':'Enter the password correctly!'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email-error': 'This E-Mail address already exists.'})
        
        account = User(email=email, username=username, bgcolor=generate_random_color())
        account.set_password(pw)
        account.save()
        return account

class LoginSerializer(serializers.ModelSerializer):
    """
    LoginSerializer is a serializer for handling user login requests.
    Fields:
        email (EmailField): The email address of the user.
        password (CharField): The password of the user, styled as a password input and write-only.
    Meta:
        model (User): The User model that this serializer is based on.
        fields (list): The fields to include in the serialization, which are 'email' and 'password'.
    Methods:
        validate(attrs):
            Validates the provided email and password.
            Authenticates the user with the given credentials.
            Raises a ValidationError if authentication fails or if email and password are not provided.
            Adds the authenticated user to the validated data.
            Returns:
                dict: The validated data including the authenticated user.
    """
    
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        trim_whitespace=False
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class CustomUserSerializer(serializers.ModelSerializer):
    """
    CustomUserSerializer is a ModelSerializer for the User model.
    Fields:
        - id: The unique identifier for the user.
        - email: The email address of the user.
        - username: The username of the user.
        - phone: The phone number of the user.
        - bgcolor: The background color associated with the user.
        - type: A custom field that always returns 'user'.
        - user: A custom field that returns the user's id.
    Methods:
        - get_type(obj): Returns the string 'user'.
        - get_user(obj): Returns the id of the user.
    """
    
    type = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'bgcolor', 'type', 'user']
        
    def get_type(self, obj):
        return 'user'

    def get_user(self, obj):
        return obj.id
