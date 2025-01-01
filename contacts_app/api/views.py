from rest_framework import viewsets, status
from rest_framework.response import Response
from contacts_app.models import Contact
from rest_framework import serializers
from .serializers import ContactSerializer
from user_auth_app.api.serializers import CustomUserSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin
from .throttling import ContactThrottle, ContactGetThrottle, ContactPostThrottle

from django.contrib.auth import get_user_model
User = get_user_model()

class ContactViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing contact instances.
    Attributes:
        queryset (QuerySet): The queryset of all contact objects.
        serializer_class (Serializer): The serializer class for contact objects.
        permission_classes (list): The list of permission classes that apply to this viewset.
    Methods:
        get_queryset(self):
            Returns a queryset of contact objects filtered by the current user.
        perform_create(self, serializer):
            Saves a new contact object with the current user as the owner.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrAdmin]
    throttle_classes = [ContactThrottle]
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_throttles(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [ContactGetThrottle]
        
        if self.action == 'create':
            return [ContactPostThrottle]
        