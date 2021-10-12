#!/usr/bin/python3
"""Class/obj MyInt inheritance of int"""


class MyInt(int):
    """Function to create new atribute"""

    def __ne__(self, other):
        return True

    def __eq__(self, other):
        return False
