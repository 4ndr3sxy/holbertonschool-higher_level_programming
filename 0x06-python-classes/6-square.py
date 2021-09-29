#!/usr/bin/python3
"""Class/module Square"""


class Square:
    """Object Square"""
    dict

    def __init__(self, size=0, position=(0, 0)):
        """Contructor"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    """get area"""
    def area(self):
        return self.__size * self.__size

    """Print Squart"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()

    """Get size"""
    def get_size(self):
        return self.__size

    """Set size"""
    def set_size(self, value):
        self.__init__(value, self.position)

    """Get position"""
    def get_position(self):
        return self.__position

    """Set position"""
    def set_position(self, value):
        self.__init__(self.__size, value)

    size = property(get_size, set_size)
    position = property(get_position, set_position)
