#!/usr/bin/python3
"""Import json"""
import json

"""Function to Convert from Python to JSON"""


def to_json_string(my_obj):
    """
        args:
            my_obj, object to convert
    """
    json_string = json.dumps(my_obj)
    return json_string
