from rest_framework import viewsets
from contacts_app.models import Contact
from .serializers import ContactSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin
from .throttling import ContactThrottle

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
        queryset = Contact.objects.filter(user=self.request.user)
        contact_param = self.request.query_params.get('contact', None)
        if contact_param is not None:
            queryset = queryset.filter(username__icontains=contact_param)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        