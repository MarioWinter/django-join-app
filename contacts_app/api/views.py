from rest_framework import viewsets
from contacts_app.models import Contact
from .serializers import ContactSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        
        return Contact.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)