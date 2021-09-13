#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    countValues = len(my_list)
    if idx < 0 or idx > countValues:
        return my_list
    my_list[idx] = element
    return my_list
