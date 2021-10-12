#!/usr/bin/python3

"""Validate is instance obj of a_class"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False
