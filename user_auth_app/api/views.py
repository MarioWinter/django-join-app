from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin
from django.contrib.auth import get_user_model
User = get_user_model()

class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    # def get_queryset(self):
    #     return User.objects.filter(user=self.request.user)


class RegistrationView(APIView):
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
                'email' : saved_account.email
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(ObtainAuthToken):
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