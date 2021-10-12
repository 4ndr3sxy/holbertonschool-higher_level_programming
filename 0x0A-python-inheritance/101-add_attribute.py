#!/usr/bin/python3
"""Function to add attrib"""


def add_attribute(objectA, name, value):
    """Add attrib in an object"""
    if not hasattr(objectA, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objectA, name, value)
