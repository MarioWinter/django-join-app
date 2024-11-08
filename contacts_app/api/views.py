from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from contacts_app.models import Contact
from .serializers import ContactSerializer
# from .permissions import IsOwnerOrAdmin


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        # Filtere die Tasks, sodass nur die des aktuellen Benutzers zurückgegeben werden
        return Contact.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)