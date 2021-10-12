#!/usr/bin/python3
"""Class/Object BaseGeometry"""


class BaseGeometry:
    """classmethod with raise if area no implemented"""
    @classmethod
    def area(self):
        raise Exception("area() is not implemented")

    """classmethod to validate value;
    if value not is an int or > 0, generate a raise"""
    @classmethod
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
