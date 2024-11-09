from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from tasks_app.models import Task, Subtasks
from .serializers import TaskSerializer, SubtasksSerializer
from .permissions import IsOwnerOrAdmin, OnlyDelete


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        # Filtere die Tasks, sodass nur die des aktuellen Benutzers zurückgegeben werden
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SubtaskViewSet(viewsets.ModelViewSet):
    queryset = Subtasks.objects.all()
    serializer_class = SubtasksSerializer
    permission_classes = [OnlyDelete]
    
    # def get_queryset(self):
    #     return Subtasks.objects.filter(user=self.request.user)
        