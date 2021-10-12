#!/usr/bin/python3
"""Import class to inheritance"""

Rectangle_ = __import__('9-rectangle').Rectangle


class Square(Rectangle_):
    """Constructor"""
    def __init__(self, size):
        self.__size = Rectangle_.integer_validator("size", size)
        super().__init__(size, size)

    """Implementation of function area"""
    def area(self):
        return self.__size * self.__size
