from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import get_user_registration_stats

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user-registration-stats/', get_user_registration_stats, name='user-registration-stats'),
]
