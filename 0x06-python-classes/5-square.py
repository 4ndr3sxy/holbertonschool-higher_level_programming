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

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__init__(value)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end='')
                print()

    size = property(get_size, set_size)
