from django.db import models
from contacts_app.models import Contact
from django.conf import settings


class Task(models.Model):
    """
    Task model representing a task in the application.
    Attributes:
        user (ForeignKey): Reference to the user who created the task.
        bucket (CharField): The bucket or category to which the task belongs.
        title (CharField): The title of the task.
        description (TextField): A detailed description of the task (optional).
        assigned (ManyToManyField): Contacts assigned to the task (optional).
        duedate (CharField): The due date of the task in 'YYYY-MM-DD' format.
        prio (CharField): The priority level of the task.
        category (CharField): The category of the task.
        subtasks (JSONField): A list of subtasks associated with the task.
    Methods:
        __str__(): Returns the string representation of the task, which is its title.
    """
    
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
