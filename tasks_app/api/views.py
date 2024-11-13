from rest_framework import viewsets

from tasks_app.models import Task
from .serializers import TaskSerializer
from user_auth_app.api.permissions import IsOwnerOrAdmin

from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrAdmin]
    
    def get_queryset(self):
        # return Task.objects.filter(user=self.request.user).prefetch_related('subtasks', 'assigned')
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class SubtaskViewSet(viewsets.ModelViewSet):
#     queryset = Subtask.objects.all()
#     serializer_class = SubtaskSerializer
#     permission_classes = [IsOwnerOrAdmin]
    
#     def get_queryset(self):
#         return Subtask.objects.filter(user=self.request.user)
        