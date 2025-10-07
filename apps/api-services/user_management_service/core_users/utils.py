from core_users.facades.user_crud_facade_impl import UserCrudFacadeImpl


# This class is in core_users/utils.py
class UserFacadesFactory:

    OBJECTS_CACHE = {}

    @staticmethod
    def get_user_crud_facade(invoked_by:str = "NotProvided"):
        if "user_crud_facade" not in UserFacadesFactory.OBJECTS_CACHE:
            UserFacadesFactory.OBJECTS_CACHE["user_crud_facade"] = UserCrudFacadeImpl()
        return UserFacadesFactory.OBJECTS_CACHE["user_crud_facade"]

