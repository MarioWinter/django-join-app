from django.urls import path, include
from .views import ContactViewSet, ContactUserListViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'combinedlist', ContactUserListViewSet, basename='combinedlist')

urlpatterns = [
     path('', include(router.urls)),
     
]