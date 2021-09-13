#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for cols in rows:
            print("{:d}{:s}".format
                  (cols, " " if cols != rows[-1] else ""), end="")
        print()
