from urllib import request
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
# from django.contrib.auth.models import User

from tasks_app.models import Task, Subtasks
from contacts_app.api.serializers import ContactSerializer
from contacts_app.models import Contact

class SubtaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(source='user_id', read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Subtasks
        fields = ['id', 'subdone', 'subtitle', 'user']


class TaskSerializer(WritableNestedModelSerializer):    
    subtasks = SubtaskSerializer(many=True, required=False)
    assigned = ContactSerializer(many=True, required=False)
    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned', 'duedate', 'prio', 'category', 'subtasks', 'user']
        read_only_fields = ['user']