from urllib import request
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth import get_user_model

from tasks_app.models import Task
from contacts_app.api.serializers import ContactSerializer
from contacts_app.models import Contact
User = get_user_model()

# class SubtaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtasks
#         fields = ['id', 'subdone', 'subtitle', 'user', 'task']
#         read_only_fields = ['user']


class TaskSerializer(serializers.ModelSerializer):
    # subtasks = SubtaskSerializer(many=True, required=False, read_only=True)
    assigned = ContactSerializer(many=True, required=False, read_only=True)
    assigned_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all(), required=False, write_only=True, source='assigned')
    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned','assigned_id', 'duedate', 'prio', 'category', 'subtasks', 'user']
        read_only_fields = ['user']
