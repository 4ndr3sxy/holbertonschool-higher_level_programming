#!/usr/bin/python3
"""Import json"""
import json

"""Function to Convert from JSON to Python"""


def from_json_string(my_str):
    """
        args:
            my_str, object to convert
    """
    json_string = json.loads(my_str)
    return json_string
