from rest_framework import serializers
from django.contrib.auth.models import User

from tasks_app.models import Task, Subtasks #TaskUser
# from contacts_app.api.serializers import ContactSerializer
# from contacts_app.models import Contact

class SubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtasks
        fields = ['subdone', 'subtitle']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtasksSerializer(many=True)
    # assigned = ContactSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned', 'duedate', 'prio', 'category', 'subtasks', 'user']
    

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        #contacts_data = validated_data.pop('assigned', [])
        task = Task.objects.create(**validated_data)
        
        for subtask_data in subtasks_data:
            Subtasks.objects.create(task=task, **subtask_data)
        return task
