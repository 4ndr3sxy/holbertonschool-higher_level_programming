#!/usr/bin/python3
def islower(c):
    asciiChar = ord(c)
    if asciiChar >= 97 and asciiChar <= 122:
        return True
    return False
