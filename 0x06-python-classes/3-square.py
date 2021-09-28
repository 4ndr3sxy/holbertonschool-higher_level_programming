#!/usr/bin/python3
"""Class/module Square"""


class Square:
    """Object Square"""
    dict

    def __init__(self, size=0):
        """Contructor"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Area of square"""
    def area(self):
        return self.__size * self.__size
