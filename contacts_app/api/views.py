from rest_framework import viewsets
from rest_framework.response import Response
from contacts_app.models import Contact
from .serializers import ContactSerializer, ContactUserListSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactUserListViewSet(viewsets.ModelViewSet):
    def list(self, request):
        user = request.user
        contacts = Contact.objects.filter(user=user)
        
        serializer = ContactUserListSerializer({
            'user': user,
            'contacts': contacts
        })
        return Response(serializer.data)
    