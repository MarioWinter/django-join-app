from django.urls import path, include
from .views import TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]