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

    """Print square"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()

    """Get position"""
    def get_position(self):
        return self.__position

    """Set position"""
    def set_position(self, value):
        self.__init__(self.__size, value)

    size = property(get_size, set_size)
    position = property(get_position, set_position)
