#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asC = ord(char)
        print("{:c}\
".format(asC-32 if asC >= 97 and asC <= 122 else asC), end='')
    print("")
