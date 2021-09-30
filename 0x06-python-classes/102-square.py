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

    """Get size"""
    def get_size(self):
        return self.__size

    """Set size"""
    def set_size(self, value):
        self.__init__(value)

    size = property(get_size, set_size)

    """Conditional =="""
    def __eq__(self, other):
        return self.area() == other.area()

    """Conditional !="""
    def __ne__(self, other):
        return self.area() != other.area()

    """Conditional >"""
    def __gt__(self, other):
        return self.area() > other.area()

    """Conditional >="""
    def __ge__(self, other):
        return self.area() >= other.area()

    """Conditional <"""
    def __lt__(self, other):
        return self.area() < other.area()

    """Conditional <="""
    def __le__(self, other):
        return self.area() <= other.area()
