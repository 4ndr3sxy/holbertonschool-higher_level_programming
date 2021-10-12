#!/usr/bin/python3
"""Class/object Student"""


def append_after(filename="", search_string="", new_string=""):
    inputfile = open(filename, 'r').readlines()
    write_file = open(filename, 'w')
    for line in inputfile:
        write_file.write(line)
        if search_string in line:
            write_file.write(new_string)
    write_file.close()
