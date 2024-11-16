from rest_framework import serializers
from user_auth_app.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'location']

class RegistrationSerializer(serializers.ModelSerializer):
    
    repeated_password = serializers.CharField(write_only=True)
        
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password', 'first_name', 'last_name']
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
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        
        if pw != repeated_pw:
            raise serializers.ValidationError({'password-error':'Enter the password correctly!'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email-error': 'This email address already exists.'})
        
        account = User(email=email, username=username, first_name=first_name, last_name=last_name)
        account.set_password(pw)
        account.save()
        return account