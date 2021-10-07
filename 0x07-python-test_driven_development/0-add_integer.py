#!/usr/bin/python3
"""Function add_integer sum two numbers"""


def add_integer(a, b=98):
    """Conditional to know type of variables"""
    if ((type(a) is not int and type(a) is not float) or
            (type(b) is not int and type(b) is not float)):
        raise TypeError("{} must be an integer".format(
            "a" if type(a) is not int and type(a) is not float else "b"))

    """Convert a to int"""
    if type(a) is float:
        a = int(a)
    """Convert b to int"""
    if type(b) is float:
        b = int(b)
    return a + b
