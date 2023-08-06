
from moippy.utils import constants
import base64
from requests_toolbelt import MultipartEncoder
import requests
import logging
import json
import os
import io
import datetime

DEBUG = False
TOKEN = ''
KEY = ''
ACCESS_TOKEN = ''
SANDBOX = False
BASIC = True

def DebugRequest():
    import http.client as http_client
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def Moip(private_token, private_key, access_token='', sandbox=False, debug=False):
    if debug:
        DebugRequest()
    global TOKEN
    global KEY
    global SANDBOX
    global DEBUG
    global BASIC
    global ACCESS_TOKEN

    TOKEN = private_token
    KEY = private_key
    DEBUG = debug
    SANDBOX = sandbox
    BASIC = access_token == ''
    ACCESS_TOKEN = access_token

def GenHashToken():
    return base64.b64encode(f'{TOKEN}:{KEY}'.encode("utf-8")).decode("utf-8")

def __headers(data=None, aditional_header=None):

    resource_token = data['resourceToken'] if data and 'resourceToken' in data else None

    if resource_token is None:
        resource_token = aditional_header['resourceToken'] if aditional_header and 'resourceToken' in aditional_header else None

    if BASIC:
        hash =  f'Basic {GenHashToken()}'
    elif aditional_header and 'resourceToken' in aditional_header and aditional_header['resourceToken'] and aditional_header['resourceToken'] != '':
        hash =  f'OAuth {aditional_header["resourceToken"]}'
    else:
        hash =  f'OAuth {ACCESS_TOKEN}'

    headers = {
        'Content-Type': 'application/json;charset=UTF-8' if aditional_header is None or not 'Content-Type' in aditional_header else aditional_header['Content-Type'],
        'Authorization': hash
    }

    return headers

def __Route(url):
    route = constants.ROUTE_SANDBOX if SANDBOX else constants.ROUTE_PRODUCAO
    return f'{route}{url}'

def Get(url, data={}, aditional_header=None):
    return __ValidateResponse(requests.get(__Route(url), params=data, headers=__headers(data, aditional_header)))

def Post(url, data, aditional_header=None):
    return __ValidateResponse(requests.post(__Route(url), json=data, headers=__headers(data, aditional_header)))

def Put(url, data, aditional_header=None):
    return __ValidateResponse(requests.put(__Route(url), json=data, headers=__headers(data, aditional_header)))

def Delete(url, aditional_header=None):
    return __ValidateResponse(requests.delete(__Route(url), headers=__headers(None, aditional_header)))

class MoipException(Exception):
    def __init__(self, message, detail):
        self.message = message
        self.detail = detail

def __ValidateResponse(response):
    if DEBUG:
        print(f"\n\nResponse Status Code: {response.status_code}")
        try:
            print(f"Response:\n\n {json.dumps(response.json(), indent=4)} \n\n")
        except Exception as e:
            print(f"Response:\n\n {response.text} \n\n")

    if response.status_code == 200 or response.status_code == 201:
        try:
            return response.json()
        except:
            return response.text
    elif response.status_code == 204:
        # RESPONSE OK - NO CONTENT
        return None
    elif response.status_code > 204:
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response_json = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "status": status_code,
                "error": "Internal Server Error",
                "details": [
                    {
                        "message": str(e),
                        "errorCode": "0"
                    }
                ]
            }
        raise MoipException("Moip Request Error", response_json)
