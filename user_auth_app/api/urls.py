from django.urls import path, include
from .views import RegistrationView, CustomLoginView, UserProfileViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', UserProfileViewSet, basename='profile')


urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
