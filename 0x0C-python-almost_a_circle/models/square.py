#!/usr/bin/python3
"""Import Class Rectangle"""
from models.rectangle import Rectangle

"""Class/object Square inherits of Rectangle"""


class Square(Rectangle):
    """Args - class Rectangle"""

    """Constructor"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """Get size"""
    @property
    def size(self):
        return self.width

    """Set size"""
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """Update information of the instance"""

    def update(self, *args, **kwargs):
        if args and len(args) > 0:
            dictionary_temporal = {0: "id", 1: "size",
                                   2: "_Rectangle__x",
                                   3: "_Rectangle__y"}
            for i in range(len(args)):
                value = dictionary_temporal[i]
                if value == "size":
                    self.size = args[i]
                else:
                    self.__dict__[value] = args[i]
        else:
            for key in kwargs:
                if key == "size":
                    self.size = kwargs[key]
                else:
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
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
