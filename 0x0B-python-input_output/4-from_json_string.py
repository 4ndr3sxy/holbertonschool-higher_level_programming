#!/usr/bin/python3
import json

def from_json_string(my_str):
    json_string = json.loads(my_str)
    return json_string
