import requests
from exceptions.handler import raise_exception

key = "none"
base_url = "https://apidata.mos.ru/v1/"

def get(url):
    r = requests.get(base_url + url, params={'api_key': key})
    raise_exception(r.status_code)
    return r

def post(url):
    r = requests.get(base_url + url, params={'api_key': key})
    raise_exception(r.status_code)
    return r