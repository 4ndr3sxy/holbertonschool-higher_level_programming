#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for val in my_list:
        try:
            if count >= x:
                break
            print("{:d}".format(val), end='')
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
