#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            dictionary_temporal = {0: "id", 1: "_Rectangle__width",
                                2: "_Rectangle__height", 3: "_Rectangle__x",
                                4: "_Rectangle__y"}
            for i in range(len(args)):
                value = dictionary_temporal[i]
                self.__dict__[value] = args[i]
        else:
            for key in kwargs:
                for key_dict in self.__dict__:
                    len_key = len(key) * -1
                    len_key_dict = key_dict[len_key:]
                    if key == len_key_dict:
                        self.__dict__[key_dict] = kwargs[key]
                        break

    def to_dictionary(self):
        #print(self.__dict__)
        return self.__dict__

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
