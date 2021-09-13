#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    size = len(my_string)
    for i in range(0, size):
        if my_string[i] != "c" and my_string[i] != "C":
                newString += my_string[i]
    return newString
