#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if idx >= 0 and size > idx:
        del my_list[idx]
    return my_list
