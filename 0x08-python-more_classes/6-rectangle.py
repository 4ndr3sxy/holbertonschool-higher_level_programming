#!/usr/bin/python3
"""Class/module Rectangle"""


class Rectangle:
    """Object Rectangle"""
    dict
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Constructor"""
        if type(width) is not int or type(height) is not int:
            raise TypeError("{} must be an integer".format(
                "width" if type(width) is not int else "height"))
        if width < 0 or height < 0:
            raise ValueError("{} must be >= 0".format(
                "width" if width < 0 else "height"))
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    """Get width"""
    def get_width(self):
        return self.__width

    """Set width"""
    def set_width(self, value):
        return self.__init__(value, self.__height)

    """Get height"""
    def get_height(self):
        return self.__height

    """Set height"""
    def set_height(self, value):
        return self.__init__(self.__width, value)

    """Get area of rectangle"""
    def area(self):
        return self.__height * self.__width

    """Get perimeter of rectangle"""
    def perimeter(self):
        result = (self.__width * 2) + (self.__height * 2)
        return 0 if self.__width == 0 or self.__height == 0 else result

    def __str__(self):
        print_str = ""
        nothing = ''
        if self.__width == 0 or self.__height == 0:
            return nothing
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    print_str += "#"
                print_str += "\n"
            print_str = print_str[:-1]
        return print_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    width = property(get_width, set_width)
    height = property(get_height, set_height)
