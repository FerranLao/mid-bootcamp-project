import requests
import json
from config import BASE_URL


def handle_api_error(func):
    def func_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return None
    return func_wrapper


@handle_api_error
def api_call(path: str = '/', params: str = {}):
    req = requests.get(BASE_URL+path, params=params)
    req = json.loads(req.content)
    return req
