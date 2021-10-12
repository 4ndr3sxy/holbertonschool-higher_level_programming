#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        new_dict = dict()
        for (key) in self.__dict__:
            if key in attrs:
                new_dict[key] = self.__dict__[key]
        return new_dict
