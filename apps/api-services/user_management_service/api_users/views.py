from django.shortcuts import render
from rest_framework import viewsets
from core_users.models import AppUser
from core_users.serializers import UserSerializer
from core_users.utils import UserFacadesFactory
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Get the facade instance
        user_crud_facade = UserFacadesFactory.get_user_crud_facade()

        # Prepare user data from request
        user_data = {
            'email': request.data['email'],
            'username': request.data['username'],
            'first_name': request.data.get('first_name', ''),
            'last_name': request.data.get('last_name', ''),
            'is_active': request.data.get('is_active', True)
        }

        # Call the create_user method from the facade
        user_crud_resp = user_crud_facade.create_user(user_data)

        return Response({
            'user_id': user_crud_resp.user_id,
            'email': user_crud_resp.email,
            'username': user_crud_resp.username,
            'first_name': user_crud_resp.first_name,
            'last_name': user_crud_resp.last_name,
            'is_active': user_crud_resp.is_active,
            'date_joined': user_crud_resp.date_joined
        })
