#!/usr/bin/python3
"""Function say_my_name print fist and last name"""


def say_my_name(first_name, last_name=""):
    """Args: first_name, last_name
        without return"""
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError("{} must be a string".format(
            "first_name" if type(first_name) is not str else "last_name"))
    print("My name is {} {}".format(first_name, last_name))
