from rest_framework import serializers
from tasks_app.models import Task, Subtasks #TaskUser
from django.contrib.auth.models import User

class SubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtasks
        fields = ['subdone', 'subtitle']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtasksSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned', 'duedate', 'prio', 'category', 'subtasks', 'user']
    

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            Subtasks.objects.create(task=task, **subtask_data)
        return task
