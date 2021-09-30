#!/usr/bin/python3
"""Create a Class MagicClass and use import math"""
import math


class MagicClass:
    """Constructor"""
    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
    """Get area circle"""
    def area(self):
        return (self.__radius ** 2) * math.pi

    """Get circumference circle"""
    def circumference(self):
        return self.__radius * 2 * math.pi
