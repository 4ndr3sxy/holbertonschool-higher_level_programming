#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    values_concat = ""
    count = 0
    try:
        for val in my_list:
            if count >= x:
                break
            print("{}".format(val), end='')
            count += 1
        print("{}".format(values_concat))
    except:
        print()
    return count
