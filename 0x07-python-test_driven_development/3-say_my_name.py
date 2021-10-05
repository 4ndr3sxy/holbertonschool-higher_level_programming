#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) is not str or type(last_name) is not str:
        raise TypeError("{} must be a string".format(
            "first_name" if type(first_name) is not str else "last_name"))
    print("My name is {} {}".format(first_name, last_name))
