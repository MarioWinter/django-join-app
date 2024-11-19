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


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False, read_only=True)
    subtasks_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Subtasks.objects.all(), required=False, write_only=True, source='subtasks')
    assigned = ContactSerializer(many=True, required=False, read_only=True)
    assigned_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all(), required=False, write_only=True, source='assigned')
    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned','assigned_id', 'duedate', 'prio', 'category', 'subtasks', 'subtasks_id', 'user']
        read_only_fields = ['user']
