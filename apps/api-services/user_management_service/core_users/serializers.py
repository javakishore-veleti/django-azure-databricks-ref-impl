from rest_framework import serializers
from core_users.models import AppUser, AppUserProfile


class AppUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUserProfile
        fields = ['id', 'bio', 'profile_picture']


class UserSerializer(serializers.ModelSerializer):
    profile = AppUserProfileSerializer(read_only=True)

    class Meta:
        model = AppUser
        fields = [
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
            'is_active',
            'date_joined',
            'profile'
        ]
