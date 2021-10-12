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
    write_file = open(filename, 'w')
    for line in inputfile:
        write_file.write(line)
        if search_string in line:
            write_file.write(new_string)
    write_file.close()
