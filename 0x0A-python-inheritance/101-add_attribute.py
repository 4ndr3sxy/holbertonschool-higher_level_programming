#!/usr/bin/python3

def add_attribute(objectA, name, value):
    """Add attrib in an object"""
    if hasattr(objectA, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(objectA, name, value)