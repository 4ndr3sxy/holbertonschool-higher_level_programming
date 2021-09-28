#!/usr/bin/python3
class Square:
    dict

    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise Exception("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")

    def area(self):
        return self.__size * self.__size
