from pydoc import doc
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from user_auth_app.api.permissions import ProfilePermission, IsOwnerOrAdmin
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from .serializers import RegistrationSerializer, LoginSerializer, CustomUserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class RegistrationView(APIView):
    """
    Handles user registration.
    Attributes:
        serializer_class (RegistrationSerializer): The serializer class used for user registration.
        permission_classes (list): The list of permission classes that determine access to this view.
    Methods:
        post(request):
            Handles POST requests to register a new user.
            Validates the provided data using the serializer.
            If valid, saves the new user account and generates an authentication token.
            Returns a response with the token, username, user ID, email, and background color.
            If invalid, returns a response with the validation errors.
    """
    
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'token' : token.key,
                'username' : saved_account.username,
                'user_id' : saved_account.id,
                'email' : saved_account.email,
                'bgcolor': saved_account.bgcolor
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):
    """
    CustomLoginView is a subclass of ObtainAuthToken that handles user login.
    Attributes:
        serializer_class (LoginSerializer): The serializer class used for validating login data.
        permission_classes (list): A list of permission classes that determine access to this view.
    Methods:
        post(request):
            Handles POST requests for user login.
            Validates the provided credentials using the LoginSerializer.
            If valid, returns a response containing the authentication token, username, user ID, and email.
            If invalid, returns a response with the validation errors.
    """
    
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'token' : token.key,
                'username' : user.username,
                'user_id' : user.id,
                'email' : user.email
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    UserProfileViewSet is a viewset that provides CRUD operations for the User model.
    It uses the CustomUserSerializer for serialization and ProfilePermission for access control.
    Methods:
        get_queryset(self):
            Returns a queryset of the User model filtered by the current authenticated user's ID.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [ProfilePermission]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)