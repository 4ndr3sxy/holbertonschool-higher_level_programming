#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    count_values = len(my_list)
    new_list = [None] * count_values

    for i in range(0, count_values):
        if my_list[i] % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return new_list
