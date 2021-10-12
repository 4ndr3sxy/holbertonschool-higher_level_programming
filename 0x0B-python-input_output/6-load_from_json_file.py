#!/usr/bin/python3
import json
def load_from_json_file(filename):
    with open(filename, 'r+') as f:
        read_data = f.read()
    new_json = json.loads(read_data)
    f.closed
    return new_json
