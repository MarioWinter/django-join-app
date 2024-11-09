from django.urls import path, include
from .views import TaskViewSet, SubtaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'subtask', SubtaskViewSet, basename='subtask')

urlpatterns = [
     path('', include(router.urls)),
     
]