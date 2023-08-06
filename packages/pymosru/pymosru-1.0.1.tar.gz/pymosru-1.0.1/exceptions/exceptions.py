class UnknownError(Exception):
    def __init__(self):
        super().__init__("Unknown to-send data.")

class InvalidAPIKeyError(Exception):
    def __init__(self):
        super().__init__("Invalid API key. You can find your API key here: https://apidata.mos.ru/")

class ServerError(Exception):
    def __init__(self):
        super().__init__("Internal server error. Try to edit your filter/to-find function etc.")

class ServerStatusCodeError(Exception):
    def __init__(self):
        super().__init__("Server didn't return a response. Try again later.")

class InvalidDatasetID(Exception):
    def __init__(self, obj_id):
        super().__init__(f"Dataset with ID {obj_id} doesn't exist.")

class InvalidCategoryID(Exception):
    def __init__(self, obj_id):
        super().__init__(f"Category with ID {obj_id} doesn't exist.")

class InvalidAppID(Exception):
    def __init__(self, obj_id):
        super().__init__(f"App with ID {obj_id} doesn't exist.")