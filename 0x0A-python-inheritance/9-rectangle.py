#!/usr/bin/python3
"""Import class to inheritance"""

BaseGeometry_ = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry_):
    """Constructor"""
    def __init__(self, width, height):
        self.__width = BaseGeometry_.integer_validator("width", width)
        self.__height = BaseGeometry_.integer_validator("height", height)

    """Implementation function area()"""
    def area(self):
        return self.__width * self.__height

    """Print information basic"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
