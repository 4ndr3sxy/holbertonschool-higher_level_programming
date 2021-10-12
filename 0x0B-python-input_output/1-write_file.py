#!/usr/bin/python3
"""Function to write in a file, with used"""


def write_file(filename="", text=""):
    """
        args:
            filename, name of file to write
            text, text to write in the file
    """
    with open(filename, 'w') as f:
        count_chars = f.write(text)
    return count_chars
