from django.urls import path,include
from .views import RegistrationView, CustomLoginView, UserProfileView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'profile', UserProfileView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    #path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    #path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
