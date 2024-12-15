from django.db import models
from contacts_app.models import Contact
from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    bucket = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    assigned = models.ManyToManyField(Contact, related_name='assigned_tasks', blank=True)
    duedate = models.CharField(max_length=10)
    prio = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    subtasks = models.JSONField(default=list)
    
    def __str__(self):
        return self.title
