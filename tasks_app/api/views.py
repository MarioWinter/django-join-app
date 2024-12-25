from rest_framework import viewsets

from tasks_app.models import Task
from .serializers import TaskSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    """
    TaskViewSet is a viewset for handling CRUD operations on Task objects.
    Attributes:
        serializer_class (TaskSerializer): The serializer class used for validating and deserializing input, and for serializing output.
        permission_classes (list): A list of permission classes that determine whether a user can access the view.
    Methods:
        get_queryset(self):
            Returns a queryset of Task objects filtered by the current user.
        perform_create(self, serializer):
            Saves a new Task object with the current user set as the owner.
    """
    
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    
    @extend_schema(
        parameters=[
            OpenApiParameter("id", int, description='The ID of the task')
        ]
    )
    def get_queryset(self) -> Task:
        return Task.objects.filter(user=self.request.user)
        

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

        