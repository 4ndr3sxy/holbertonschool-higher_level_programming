#!/usr/bin/python3
"""Import class Base()"""
from models.base import Base

"""Class/object Rectangle, inherits of class Base"""


class Rectangle(Base):
    """Args - class Base()"""

    """Constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """get width"""
    @property
    def width(self):
        return self.__width

    """Set width"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    """Get height"""
    @property
    def height(self):
        return self.__height

    """Set height"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    """Get x"""
    @property
    def x(self):
        return self.__x

    """Set x"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    """Get y"""
    @property
    def y(self):
        return self.__y

    """Set y"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    """Return area of rectangle"""
    def area(self):
        return self.height * self.width

    """Print a Rectanlge with a char '#' """
    def display(self):
        print("\n" * self.__y, end='')
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    """Update information of the instance"""
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

    """Return __dict__"""
    def to_dictionary(self):
        return self.__dict__

    """Standar print()"""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
