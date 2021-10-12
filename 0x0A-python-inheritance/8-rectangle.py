#!/usr/bin/python3
"""Import class to inheritance"""

BaseGeometry_ = __import__('7-base_geometry').BaseGeometry

"""Class/object REctangle that inherits of BaseGeometry"""


class Rectangle(BaseGeometry_):
    """Constructor with inheritance"""
    def __init__(self, width, height):
        self.__width = BaseGeometry_.integer_validator("width", width)
        self.__height = BaseGeometry_.integer_validator("height", height)
