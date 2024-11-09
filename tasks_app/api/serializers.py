from rest_framework import serializers
from django.contrib.auth.models import User

from tasks_app.models import Task, Subtasks #TaskUser
# from contacts_app.api.serializers import ContactSerializer
# from contacts_app.models import Contact

class SubtasksSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    class Meta:
        model = Subtasks
        fields = ['id', 'subdone', 'subtitle', 'task']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtasksSerializer(many=True)
    # assigned = ContactSerializer(many=True)
    #zum Testen
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['id', 'bucket', 'title', 'description', 'assigned', 'duedate', 'prio', 'category', 'subtasks', 'user']
    

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', None)
        #contacts_data = validated_data.pop('assigned', [])
        task = Task.objects.create(**validated_data)
        
        for subtask_data in subtasks_data:
            Subtasks.objects.create(task=task, **subtask_data)
        return task
    
    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        subtasks_data = validated_data.pop('subtasks', None)
        if subtasks_data is not None:
            instance.subtasks.all().delete()
            for subtask_data in subtasks_data:
                Subtasks.objects.create(task=instance, **subtask_data)

        return instance
    
    def partial_update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        subtasks_data = validated_data.pop('subtasks', None)
        if subtasks_data is not None:
            for subtask_data in subtasks_data:
                subtask_id = subtask_data.get('id')
                if subtask_id:
                    subtask = Subtasks.objects.get(id=subtask_id, task=instance)
                    for key, value in subtask_data.items():
                        setattr(subtask, key, value)
                    subtask.save()
                else:
                    Subtasks.objects.create(task=instance, **subtask_data)
        return instance