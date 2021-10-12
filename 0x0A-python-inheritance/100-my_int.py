#!/usr/bin/python3
"""Class/obj MyInt inheritance of int"""


class MyInt(int):
    """Function to create new atribute"""

    def __new__(cls, number):
        return super(MyInt, cls).__new__(cls, number)
