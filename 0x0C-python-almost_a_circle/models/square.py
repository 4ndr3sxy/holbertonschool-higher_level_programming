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
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return __dict__"""
        """Return __dict__"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key[:12] == "_Rectangle__":
                temp_values = key[12:]
                if temp_values == "height" or temp_values == "width":
                    new_dict["size"] = value
                else:
                    new_dict[key[12:]] = value
            else:
                new_dict[key] = value
        return new_dict

    def __str__(self):
        """Standar print()"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
