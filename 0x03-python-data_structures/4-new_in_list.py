#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    countValues = len(my_list)
    if idx < 0 or idx > countValues - 1:
        return my_list
    newList = [None] * countValues
    for i in range(0, countValues):
        if i == idx:
            newList[i] = element
        else:
            newList[i] = my_list[i]
    return newList
