from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from user_auth_app.api.utils import generate_random_color
User = get_user_model()



class RegistrationSerializer(serializers.ModelSerializer):
    
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
    type = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'bgcolor', 'type', 'user']
        
    def get_type(self, obj):
        return 'user'

    def get_user(self, obj):
        return obj.id
