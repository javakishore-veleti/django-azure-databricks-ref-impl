from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_users.views import UserViewSet

# Create a router and register the UserViewSet
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='appuser')

# Define URL patterns for this app
urlpatterns = [
    path('', include(router.urls)),
]
