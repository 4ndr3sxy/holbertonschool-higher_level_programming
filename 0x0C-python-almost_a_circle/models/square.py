#!/usr/bin/python3
"""Import Class Rectangle
Class/object Square inherits of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Args - class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update information of the instance"""
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

    def to_dictionary(self):
        """Return __dict__"""
        return self.__dict__

    def __str__(self):
        """Standar print()"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
