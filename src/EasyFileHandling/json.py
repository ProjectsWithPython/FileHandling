import json
from typing import Union
from EasyFileHandling.errors.error import *

class JsonHandler:
    """JsonHandler it reads, converts and writes but remeber file should be json only!"""

    def __init__(self, _filename):
        self._filename = _filename

    def write_to_json(self, obj: Union[dict, list]) -> None:
        """Writes to json file"""
        try:
            with open(self._filename, "w") as f:
                if type(obj) == list or type(obj) == dict:
                    json.dump(obj, f)
                else:
                    raise JSONTakesListOrDict()
        except:
            raise FileNotFoundError()

    def append_to_json(self, obj: Union[dict, list]) -> None:
        """Appends to json file"""
        try:
            with open(self._filename, "a") as f:
                if type(obj) == list or type(obj) == dict:
                    json.dump(obj, f)
                else:
                    raise JSONTakesListOrDict()
        except:
            raise UnexpectedError()

    def read_json_file(self) -> Union[dict, list]:
        try:
            with open(self._filename, "r") as f:
                x = json.load(f)
                return x
        except:
            raise UnexpectedError()