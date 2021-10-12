#!/usr/bin/python3
"""Function to load a simple data of the a class """


def class_to_json(obj):
    """
        args:
            obj, object type class
    """
    obj_info = obj.__dict__
    return obj_info
