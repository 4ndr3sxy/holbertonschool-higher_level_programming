#!/usr/bin/python3
"""Import class to inheritance"""
Rectangle_ = __import__('9-rectangle').Rectangle

"""Class/object Square that inherits of Rectangle"""


class Square(Rectangle_):
    """Constructor"""
    def __init__(self, size):
        self.__size = Rectangle_.integer_validator("size", size)

    
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size