#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    result = 0
    result_div = 0
    for values in my_list:
        result += (values[0] * values[1])
        result_div += values[1]
    return result / result_div
