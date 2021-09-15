#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    validator = 1
    while validator == 1:
        for keys, values in a_dictionary.items():
            if values == value:
                validator = 1
                del(a_dictionary[keys])
                break
            else:
                validator = 0
    return a_dictionary
