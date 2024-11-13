from rest_framework import serializers
# from django.contrib.auth.models import User

from tasks_app.models import Task
# from contacts_app.api.serializers import ContactSerializer
# from contacts_app.models import Contact

# class SubtaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Subtask
#         fields = ['id', 'subdone', 'subtitle', 'user']


class TaskSerializer(serializers.ModelSerializer):
    #assigned = ContactSerializer(many=True, read_only=True) 
    #subtasks = SubtaskSerializer(many=True, read_only=True)

     # Diese Felder werden für POST/PUT/PATCH verwendet
    # subtask_id = serializers.PrimaryKeyRelatedField(
    #     many=True, write_only=True, queryset=Subtask.objects.all(), source='subtasks'
    # )
    # assigned_id = serializers.PrimaryKeyRelatedField(
    #     many=True, write_only=True, queryset=Contact.objects.all(), source='assigned'
    # )

    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned', 'duedate', 'prio', 'category', 'subtask', 'user']
        read_only_fields = ['user']

    # def create(self, validated_data):
    #     # subtasks = validated_data.pop('subtasks', [])
    #     assigned = validated_data.pop('assigned', [])
    #     task = Task.objects.create(**validated_data)
    #     # task.subtasks.set(subtasks)
    #     task.assigned.set(assigned)
    #     return task

    # def update(self, instance, validated_data):
    #     # subtasks = validated_data.pop('subtasks', None)
    #     assigned = validated_data.pop('assigned', None)
        
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
        
    #     # if subtasks is not None:
    #     #     instance.subtasks.set(subtasks)
    #     if assigned is not None:
    #         instance.assigned.set(assigned)
        
    #     instance.save()
    #     return instance