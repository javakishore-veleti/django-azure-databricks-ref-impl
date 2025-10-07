from core_users.models import AppUser, AppUserProfile
import socket
import uuid
from datetime import datetime


# These classes are in app_common/dtos/dtos_users.py
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

    def __int__(self):
        pass

    def __init__(self, user_id, email, username, first_name, last_name, is_active, date_joined):
        self.user_id: str = user_id
        self.email: str = email
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.is_active: bool = is_active
        self.date_joined = date_joined
        self.users_list = []  # To be used in list responses
        self.user_by_id: AppUser = AppUser()
        self.user_profile_by_id: AppUserProfile = AppUserProfile()


class UserEventInfo:
    def __init__(self, event_type: str, app_user_dict: dict, event_business_process_id: str = None):
        self.event_date = datetime.utcnow().isoformat(timespec='microseconds')
        self.event_host_name = socket.gethostname()
        self.event_id = str(uuid.uuid4())
        self.event_business_process_id = event_business_process_id or str(uuid.uuid4())
        self.event_type = event_type  # 'CREATE', 'UPDATE', 'DELETE', etc.
        self.app_user = app_user_dict  # Serialized AppUser dict

    def to_json(self):
        """Return a JSON-serializable dict version of this event."""
        return {
            "event_date": self.event_date,
            "event_host_name": self.event_host_name,
            "event_id": self.event_id,
            "event_business_process_id": self.event_business_process_id,
            "event_type": self.event_type,
            "app_user": self.app_user,
        }
