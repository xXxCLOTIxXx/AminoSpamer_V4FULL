import base64
import hmac
import json
import os
import requests

from functools import reduce
from base64 import b64decode
from hashlib import sha1

def generate_device_id() -> str:
    device = requests.get(f"https://ed-generators.herokuapp.com/device").text
    return device
#Credit by badTm : Alert and Human
#Note : Spam = delete api ..

def generate_signature(data: str):
    signature = requests.get(f"https://ed-generators.herokuapp.com/signature?data={data}").text
    return signature
def generate_device_info():
    return {
        "device_id": generate_device_id(),
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.5.33562)"
    }

# okok says: please use return annotations :(( https://www.python.org/dev/peps/pep-3107/#return-values

def decode_sid(sid: str) -> dict:
    return json.loads(b64decode(reduce(lambda a, e: a.replace(*e), ("-+", "_/"), sid + "=" * (-len(sid) % 4)).encode())[1:-20].decode())

def sid_to_uid(SID: str) -> str: return decode_sid(SID)["2"]

def sid_to_ip_address(SID: str) -> str: return decode_sid(SID)["4"]