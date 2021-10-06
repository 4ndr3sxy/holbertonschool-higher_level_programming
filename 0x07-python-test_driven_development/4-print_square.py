#!/usr/bin/python3
"""Function print_square, print a square"""


def print_square(size):
    """Args: size
        without return"""
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(str("#" * size))
