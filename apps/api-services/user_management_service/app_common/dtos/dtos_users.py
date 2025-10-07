from core_users.models import AppUser, AppUserProfile

# Thease class are in app_common/dtos/dtos_users.py
# Data Transfer Objects (DTOs) for User operations
class UserCrudReq:
    def __init__(self, email, username, first_name=None, last_name=None, is_active=True, user_id=None):
        self.email: str = email
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.is_active: bool = is_active
        self.user_id: str = user_id


class UserCrudResp:
    def __init__(self, user_id, email, username, first_name, last_name, is_active, date_joined):
        self.user_id: str = user_id
        self.email: str = email
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.is_active:bool = is_active
        self.date_joined = date_joined
        self.users_list = []  # To be used in list responses
        self.user_by_id: AppUser = None
        self.user_profile_by_id: AppUserProfile = None
