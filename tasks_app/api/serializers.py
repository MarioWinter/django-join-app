from rest_framework import serializers
from tasks_app.models import Task, TaskUser

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUser
        fields = ['task', 'user', 'role', 'addedTask_date']