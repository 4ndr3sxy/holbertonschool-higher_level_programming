#!/usr/bin/python3
"""Validate is instance obj of a_class"""


def is_kind_of_class(obj, a_class):
    """obj and a_class used"""
    if isinstance(obj, a_class):
        return True
    return False
