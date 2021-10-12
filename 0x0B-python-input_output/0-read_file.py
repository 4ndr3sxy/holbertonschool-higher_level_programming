#!/usr/bin/python3
"""Function to read a file, with used"""


def read_file(filename=""):
    """
        args: filename, name of file to read
    """
    with open(filename) as f:
        read_data = f.read()
    print(read_data, end='')
    f.closed
