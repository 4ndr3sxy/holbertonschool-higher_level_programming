#!/usr/bin/python3
"""Class/object Student"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
        filename, name of the file
        search_string, string to find in a file
        new_string, set this 'new_string' after 'search_string'
    """
    inputfile = open(filename, 'r').readlines()
    with open(filename, 'w') as infile:
        for line in inputfile:
            infile.write(line)
            if search_string in line:
                infile.write(new_string)
