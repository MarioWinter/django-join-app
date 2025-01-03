from django.urls import path, include
from .views import ContactViewSet
from user_auth_app.api.views import UserProfileViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [
     path('', include(router.urls)),
     
]