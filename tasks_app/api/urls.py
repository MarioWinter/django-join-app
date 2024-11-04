from django.urls import path
from .views import TaskList

urlpatterns = [
     path('tasks/', TaskList.as_view(), name='task-list'),
]