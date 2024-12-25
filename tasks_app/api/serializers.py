from urllib import request
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from django.contrib.auth import get_user_model

from tasks_app.models import Task
from contacts_app.api.serializers import ContactSerializer
from contacts_app.models import Contact
User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    """
    TaskSerializer is a ModelSerializer for the Task model. It serializes and deserializes Task instances.
    Fields:
        - id: IntegerField, read-only. The primary key of the task.
        - bucket: CharField. The bucket to which the task belongs.
        - title: CharField. The title of the task.
        - description: CharField. The description of the task.
        - assigned: ContactSerializer, read-only. A list of contacts assigned to the task.
        - assigned_id: PrimaryKeyRelatedField, write-only. A list of primary keys of contacts to be assigned to the task.
        - duedate: DateTimeField. The due date of the task.
        - prio: IntegerField. The priority of the task.
        - category: CharField. The category of the task.
        - subtasks: CharField. The subtasks of the task.
        - user: UserField, read-only. The user who created the task.
    Meta:
        - model: Task. The model that is being serialized.
        - fields: List of fields to be included in the serialization.
        - read_only_fields: List of fields that are read-only.
    """
    
    assigned = ContactSerializer(many=True, required=False, read_only=True)
    assigned_id = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all(), required=False, write_only=True, source='assigned')
    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned','assigned_id', 'duedate', 'prio', 'category', 'subtasks', 'user']
        read_only_fields = ['user']
