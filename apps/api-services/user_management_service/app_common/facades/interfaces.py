# This class is in app_common/facades/interfaces.py
class AppUserFacadeInterface:
    def get_user(self, user_id: int):
        raise NotImplementedError

    def create_user(self, user_data: dict):
        raise NotImplementedError

    def update_user(self, user_id: int, user_data: dict):
        raise NotImplementedError

    def delete_user(self, user_id: int):
        raise NotImplementedError