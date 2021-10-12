#!/usr/bin/python3
"""Function to write/append in a file, with used"""


def append_write(filename="", text=""):
    """
        args:
            filename, name of file to append text
            text, text to append in the file
    """
    with open(filename, 'a') as f:
        count_chars = f.write(text)
    return count_chars
