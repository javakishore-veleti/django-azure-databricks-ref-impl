from app_common.facades.interfaces import AppUserFacadeInterface
from core_users.models import AppUser, AppUserProfile
from app_common.dtos.dtos_users import UserCrudReq, UserCrudResp


class UserCrudFacadeImpl(AppUserFacadeInterface):

    def get_user(self, user_id: int) -> UserCrudResp:
        """
        Retrieves the user by ID and returns the user data in the response object.
        """
        try:
            app_user = AppUser.objects.get(id=user_id)
            app_user_profile = AppUserProfile.objects.get(user=app_user)

            # Construct the response object
            user_resp = UserCrudResp(
                user_id=app_user.id,
                email=app_user.email,
                username=app_user.username,
                first_name=app_user.first_name,
                last_name=app_user.last_name,
                is_active=app_user.is_active,
                date_joined=app_user.date_joined
            )
            user_resp.user_by_id = app_user
            user_resp.user_profile_by_id = app_user_profile
            return user_resp
        except AppUser.DoesNotExist:
            return None  # Handle user not found

    def create_user(self, user_data: dict) -> UserCrudResp:
        """
        Creates a new user with the provided data and returns a response object.
        """
        user_crud_req = UserCrudReq(
            email=user_data.get('email'),
            username=user_data.get('username'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            is_active=user_data.get('is_active', True)
        )

        # Create the user
        app_user = AppUser.objects.create(
            email=user_crud_req.email,
            username=user_crud_req.username,
            first_name=user_crud_req.first_name,
            last_name=user_crud_req.last_name,
            is_active=user_crud_req.is_active
        )

        # Create a profile for the user
        app_user_profile = AppUserProfile.objects.create(user=app_user)

        # Return the response object
        return UserCrudResp(
            user_id=app_user.id,
            email=app_user.email,
            username=app_user.username,
            first_name=app_user.first_name,
            last_name=app_user.last_name,
            is_active=app_user.is_active,
            date_joined=app_user.date_joined
        )

    def update_user(self, user_id: int, user_data: dict) -> UserCrudResp:
        """
        Updates an existing user and returns the updated response object.
        """
        try:
            app_user = AppUser.objects.get(id=user_id)
            app_user.email = user_data.get('email', app_user.email)
            app_user.username = user_data.get('username', app_user.username)
            app_user.first_name = user_data.get('first_name', app_user.first_name)
            app_user.last_name = user_data.get('last_name', app_user.last_name)
            app_user.is_active = user_data.get('is_active', app_user.is_active)
            app_user.save()

            # Optionally update the user profile if needed
            app_user_profile = AppUserProfile.objects.get(user=app_user)
            app_user_profile.save()  # Save any changes to the profile if necessary

            # Return updated response
            return UserCrudResp(
                user_id=app_user.id,
                email=app_user.email,
                username=app_user.username,
                first_name=app_user.first_name,
                last_name=app_user.last_name,
                is_active=app_user.is_active,
                date_joined=app_user.date_joined
            )
        except AppUser.DoesNotExist:
            return None  # Handle user not found

    def delete_user(self, user_id: int) -> bool:
        """
        Deletes a user by ID and returns success status.
        """
        try:
            app_user = AppUser.objects.get(id=user_id)
            app_user.delete()  # Deletes both user and related profile (if cascade delete is set)
            return True
        except AppUser.DoesNotExist:
            return False  # Handle user not found
