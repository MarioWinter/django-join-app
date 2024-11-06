from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    bucket = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    assigned = models.JSONField(default=list)
    #assigned = models.ManyToManyField(Contact, related_name='assigned_tasks', blank=True)
    duedate = models.CharField(max_length=10)
    prio = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    #subtask = models.JSONField(blank=True, null=True)
    

    def __str__(self):
        return self.title


class Subtasks(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    subdone = models.BooleanField(blank=True, default=False)
    subtitle = models.CharField(max_length=1000)

    def __str__(self):
        return self.subtitle
    
# class TaskUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     role = models.CharField(max_length=50, blank=True, null=True)
#     addedTask_date = models.DateField(auto_now_add=True)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=['user', 'task'], name='unique_user_task')
#         ]

#     def __str__(self):
#         return f"{self.user.username} - {self.task.title}" 
    
    
    
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