#!/usr/bin/python3
"""Import json"""
import json

"""Function to load a file .json"""


def load_from_json_file(filename):
    """
        args:
            filename, name of file .json
    """
    with open(filename, 'r+') as f:
        read_data = f.read()
    new_json = json.loads(read_data)
    f.closed
    return new_json
