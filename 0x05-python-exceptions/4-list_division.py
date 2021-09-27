#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            validate = False
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            validate = True
        except TypeError:
            print("wrong type")
            validate = True
        except IndexError:
            print("out of range")
            validate = True
        finally:
            if not validate:
                new_list.append(result)
            else:
                new_list.append(0)
    return new_list
