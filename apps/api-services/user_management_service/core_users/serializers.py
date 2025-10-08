from rest_framework import serializers
from core_users.models import AppUser, AppUserProfile


class AppUserProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, required=False)  # String-based UUID primary key

    class Meta:
        model = AppUserProfile
        fields = ['id', 'user', 'bio']  # Include the custom 'id' field
        read_only_fields = ['user']  # Assuming 'user' is a ForeignKey, you can leave it read-only for serialization


class UserSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=36, required=False)  # String-based UUID primary key
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
