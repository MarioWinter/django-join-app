from rest_framework import viewsets, status
from rest_framework.response import Response
from contacts_app.models import Contact
from rest_framework import serializers
from .serializers import ContactSerializer, ContactUserListSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin

from django.contrib.auth import get_user_model
User = get_user_model()

class ContactViewSet(viewsets.ModelViewSet):
    
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        
        return Contact.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class ContactViewSet(viewsets.ModelViewSet):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     permission_classes = [IsOwnerOrAdmin]

#     def get_queryset(self):
#         return Contact.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#GGF Löschen
class ContactUserListViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        contacts = self.get_queryset().filter(user=user)
        
        user_serializer = CustomUserSerializer(user)
        contacts_serializer = self.get_serializer(contacts, many=True)
        
        combined_data = [user_serializer.data] + contacts_serializer.data
        return Response(combined_data)
    