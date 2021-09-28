#!/usr/bin/python3
class Square:
    dict

    def __init__(self, size=0, position=(0, 0)):
        try:
            self.__size = size
            self.__position = position
            if size < 0:
                raise Exception("size must be >= 0")
            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        except TypeError:
            raise Exception("size must be an integer")

    def area(self):
        return self.__size * self.__size

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

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__init__(value)

    def get_position(self):
        return self.__position

    def set_position(self, value):
        self.__init__(self.__size, value)

    size = property(get_size, set_size)
    position = property(get_position, set_position)
