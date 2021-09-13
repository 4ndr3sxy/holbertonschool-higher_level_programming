#!/usr/bin/python3
def element_at(my_list, idx):
    countValues = len(my_list)
    if idx < 0 or idx > countValues:
        return
    valueIndex = my_list[idx]
    return valueIndex
