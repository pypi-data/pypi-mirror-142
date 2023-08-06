import inspect
import json
import re
import traceback
from pprint import pprint

import requests

from maxoptics.config import Config
from maxoptics.error import ConnectTimeoutError, MaxRetryError, NewConnectionError, PostResultFailedError
from maxoptics.utils.__pyfuture__ import fstr
from maxoptics.utils.base import error_print, info_print

BETA = Config.BETA


class HttpIO:
    def __init__(self, url_key, api_config_key, port_config_key) -> None:
        super().__init__()
        self.api_url = get_valid_api(url_key, api_config_key, port_config_key)

    def post(self, url="", __base_params__={}, **kwargs):
        if BETA:
            info_print(f"{url = } token %s" % (kwargs.get("token")))
            print("url", url)
            print("__base_params__", __base_params__)
            pprint(kwargs)
        try:
            kwargs.update(__base_params__)
            if url:
                r = requests.post(
                    self.api_url % url,
                    data=json.dumps(kwargs),
                    headers={"Content-Type": "application/json", "Connection": "close"},
                )
            else:
                r = requests.post(
                    self.api_url % (inspect.stack()[1][3]),
                    data=json.dumps(kwargs),
                    headers={"Content-Type": "application/json", "Connection": "close"},
                )
            if r.status_code == 404:
                raise PostResultFailedError()
            self.thread_status = False
            if BETA:
                pprint(r.text)
            return json.loads(r.text)
        except PostResultFailedError:
            error_print("Failed")
            error_print("Server %s API Doesn't Exist" % self.api_url)
            self.thread_status = False
            return json.loads('{"success": false, "result": {"code": 501, "msg": "Server Failed"}}')
        except (NewConnectionError, MaxRetryError, ConnectTimeoutError):
            error_print("Server %s May " % self.api_url)
            error_print("Failed")
            self.thread_status = False
            return json.loads('{"success": false, "result": {"code": 501, "msg": "Server Failed"}}')
        except requests.exceptions.ConnectionError:
            error_print("Failed")
            self.thread_status = False
            error_print("Cannot connect Server %s, please retry later" % self.api_url)
            return json.loads('{"success": false, "result": {"code": 502, "msg": "Server Failed"}}')
        except requests.exceptions.ChunkedEncodingError:
            error_print("Failed")
            error_print("ChunkedEncodingError -- Retry later")
            self.thread_status = False
            return json.loads('{"success": false, "result": {"code": 503, "msg": "Server Error"}}')
        except Exception as e:
            error_print(f"{inspect.stack()[1][3]} Failed")
            error_print("Unfortunately -- Retry later", e)
            traceback.print_exc()
            self.thread_status = False
            return json.loads('{"success": false, "result": {"code": 509, "msg": "Server Error"}}')


def get_valid_api(url_key, api_config_key, port_config_key):
    url_template = getattr(Config, url_key)
    api_address = getattr(Config, api_config_key)
    port = getattr(Config, port_config_key)
    if not api_address:
        while True:
            api_address = input("Server:\n").strip()
            if re.match("^http(s)?://([A-Za-z0-9-]+[\\./])+[A-Za-z0-9]+(/)?$", api_address):
                assert len(api_address) > 1
                api_address = fstr(api_address)
                api_address = api_address.removeprefix("https://").removeprefix("http://").removesuffix("/")
                api_address = api_address.__str__
                break

            elif re.match("^([A-Za-z0-9-]+[\\./])+[A-Za-z0-9]+$", api_address):
                if ":" in api_address and api_address.count(":") == 1:
                    api_address, port = api_address.split(":")
                break

    setattr(Config, api_config_key, api_address)
    setattr(Config, port_config_key, port)

    api_url = url_template.format(api_address, port)
    return api_url
