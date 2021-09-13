#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return my_list
    size = len(my_list)
    if size < idx or idx < 0:
        return my_list
    del my_list[idx]
    return my_list
