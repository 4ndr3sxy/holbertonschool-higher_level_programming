#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dictionary_sorted = a_dictionary
    for keys, values in sorted(dictionary_sorted.items()):
        print("{:s}: {}".format(keys, values))
