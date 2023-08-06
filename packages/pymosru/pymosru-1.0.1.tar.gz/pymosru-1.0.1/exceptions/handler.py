from .exceptions import *

exceptions = {404: UnknownError(), 403: InvalidAPIKeyError(), 500: ServerError(), 406: ServerStatusCodeError(), 408: ServerStatusCodeError(), 200: None}

def raise_exception(code):
    if not code == 200:
        raise exceptions[code]
