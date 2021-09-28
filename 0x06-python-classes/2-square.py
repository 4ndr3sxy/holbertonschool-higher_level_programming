#!/usr/bin/python3
"""Class/module Square"""


class Square:
    """Object Square"""
    dict

    def __init__(self, size=0):
        """Contructor"""
        try:
            self.__size = size
            if size < 0:
                raise Exception("size must be >= 0")
        except TypeError:
            raise Exception("size must be an integer")
