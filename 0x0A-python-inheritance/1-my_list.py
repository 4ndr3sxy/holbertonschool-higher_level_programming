#!/usr/bin/python3
"""Class MyList, Inheritance of object list"""


class MyList(list):
    """create copy of the self and sort and print this copy"""
    def print_sorted(self):
        new_list = []
        new_list = self.copy()
        print(sorted(new_list))
