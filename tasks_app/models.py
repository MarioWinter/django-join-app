from django.db import models
from django.contrib.auth.models import User
from contacts_app.models import Contact


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    bucket = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # assigned = models.ManyToManyField(Contact, related_name='assigned_tasks', blank=True)
    assigned = models.JSONField(default=list)
    duedate = models.CharField(max_length=10)
    prio = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    subtask = models.JSONField(default=list)
    
    def __str__(self):
        return self.title


# class Subtask(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subdone = models.BooleanField(blank=True, default=False)
#     subtitle = models.CharField(max_length=1000)

#     def __str__(self):
#         return self.subtitle
      
    
# addedTasks.push({
#     id: setNewTask,
#     bucket: "to-do",
#     title: enter_title_field.value,
#     description: enter_description_field.value,
#     assigned: newAssigned,
#     duedate: date_field.value,
#     prio: selectedPriority,
#     category: select_category_field.value,
#     subtask: addedSubtasks,