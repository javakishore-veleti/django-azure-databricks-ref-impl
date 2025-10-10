class DLSetupReq:
    def __init__(self, model_name: str, dataset_name: str, epochs: int, batch_size: int):
        self.model_name = model_name
        self.dataset_name = dataset_name
        self.epochs = epochs
        self.batch_size = batch_size

class DLSetupResp:
    def __init__(self, success: bool, message: str, model_id: str = None):
        self.success = success
        self.message = message
        self.model_id = model_id