#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = sum(number for number in set(my_list))
    return result
