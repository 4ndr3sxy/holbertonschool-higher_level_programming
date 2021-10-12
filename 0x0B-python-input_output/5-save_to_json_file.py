#!/usr/bin/python3
"""Import json"""
import json

"""Function to Convert from Python to JSON and save in a file"""


def save_to_json_file(my_obj, filename):
    """
        args:
            my_obj, object to save
            filename, name of file .json
    """
    with open(filename, 'w+') as f:
        f.write(json.dumps(my_obj))
    f.closed
