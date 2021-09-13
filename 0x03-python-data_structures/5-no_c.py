#!/usr/bin/python3
def no_c(my_string):
    size = len(my_string)
    cs = 0
    for c in my_string:
        if c == "c" or c == "C":
            cs += 1
    for i in range(0, size - cs):
        if my_string[i] == "c" or my_string[i] == "C":
            my_string = my_string[:i] + my_string[i + 1:]
    return my_string
