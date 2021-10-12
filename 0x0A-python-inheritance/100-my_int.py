#!/usr/bin/python3
class MyInt(int):
    def __new__(cls, number, *args, **kwargs):
        return  super(MyInt, cls).__new__(cls, number)