#!/usr/bin/python3
"""returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    init_pascal = 1
    i = 0
    j = 0
    triangle = []
    while i < n:
        pascal = []
        while j < i+1:
            if j == 0 or j >= len(triangle):
                pascal.append(init_pascal)
            else:
                new_pascal = triangle[i-1][j] + triangle[i-1][j-1]
                pascal.append(new_pascal)
            j += 1
        triangle.append(pascal)
        j = 0
        i += 1
    return triangle
