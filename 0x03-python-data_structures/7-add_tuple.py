#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    size_one = len(tuple_a)
    size_two = len(tuple_b)
    one = one_t = two = two_t = 0
    if size_one == 1:
        one = tuple_a[0]
    if size_two == 1:
        two = tuple_b[0]
    if size_one == 2:
        one = tuple_a[0]
        one_t = tuple_a[1]
    if size_two == 2:
        two = tuple_b[0]
        two_t = tuple_b[1]

    add_one = one + two
    add_two = one_t + two_t
    return add_one, add_two
