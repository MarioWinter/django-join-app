from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from tasks_app.models import Task, Subtasks
from .serializers import TaskSerializer, SubtasksSerializer
from .permissions import IsOwnerOrAdmin


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        # Filtere die Tasks, sodass nur die des aktuellen Benutzers zurückgegeben werden
        return Task.objects.filter(user=self.request.user)
    
    # def create(self, request, *args, **kwargs):
    #      serializer = self.get_serializer(data=request.data)
    #      serializer.is_valid(raise_exception=True)
    #      self.perform_create(serializer)
    #      headers = self.get_success_headers(serializer.data)
    #      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)