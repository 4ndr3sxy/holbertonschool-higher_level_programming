#!/usr/bin/python3
"""Class/Object BaseGeometry"""


class BaseGeometry:
    """classmethod with raise if area no implemented"""
    @classmethod
    def area(self):
        raise Exception("area() is not implemented")
