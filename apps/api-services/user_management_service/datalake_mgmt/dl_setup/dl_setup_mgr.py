import os

from app_common.dtos.dl_setup_dtos import DLSetupReq, DLSetupResp


class DLSetupManager:
    def setup_medallion_architecture(self, dl_setup_req:DLSetupReq, dl_setup_resp:DLSetupResp) -> int:
        raise NotImplementedError("This method should be overridden by subclasses")


class DLSetupManagerImpl(DLSetupManager):
    def __init__(self):
        pass

    def setup_medallion_architecture(self, dl_setup_req:DLSetupReq, dl_setup_resp:DLSetupResp) -> int:
        # Placeholder for setup logic
        DATABRICKS_INSTANCE = os.getenv("DATABRICKS_INSTANCE")
        DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")
        return 100