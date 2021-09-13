#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for cols in rows:
            if cols != rows[-1]:
                print("{:d} ".format(cols), end="")
            else:
                print("{:d}".format(cols), end="")
        print()
