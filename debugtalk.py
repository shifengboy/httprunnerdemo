import random
import time
import uuid
import os

from httprunner import __version__
from httprunner.response import ResponseObject

from base.caeate_name import CreateName

def get_httprunner_version():
    return __version__


def get_random_request_id():
    return str(uuid.uuid4())


def get_test_host():
    if os.environ.get("TestEnv") == "pre":
        return "httprunnerdemo.net"
    else:
        return "httprunnerdemo.com"


def get_documents_num(resp: ResponseObject) -> int:
    respjson = resp.resp_obj.json()
    documents_num = len(respjson["data"]["documents"])
    print(f'$documents_num:{documents_num}')
    return documents_num


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_phone_number():
    for k in range(10):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                   "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                   "186", "187", "188", "189"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def get_name_and_sex():
    name = CreateName()
    return name.random_name_and_sex()

def get_name():
    name = CreateName()
    return name.random_name()


def get_random_number(digit: int):
    return "".join(random.choice("0123456789") for i in range(digit))



if __name__ == '__main__':
    print(get_name_and_sex())
