#!/usr/bin/python3
def matrix_divided(matrix, div):
    size = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for group in matrix:
        if size != len(group):
            raise TypeError("Each row of the matrix must \
have the same size")
        for j in group:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    new_array = list(map(lambda y: list(
        map(lambda x: round(x / div, 2), y)), matrix))
    return new_array
