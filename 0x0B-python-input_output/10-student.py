#!/usr/bin/python3

"""Class/object Student"""


class Student:
    """
    Constructor
        attributes are publics
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Return a dictionary representation with filter"""
    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for key in self.__dict__:
            if key in attrs:
                new_dict[key] = self.__dict__[key]
        return new_dict
