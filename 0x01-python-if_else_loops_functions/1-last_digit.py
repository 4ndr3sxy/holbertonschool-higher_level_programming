#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
if number < 0:
    module = -10
else:
    module = 10
lastNumber = number % module
if lastNumber > 5:
    print("Last digit of {:d} is {:d} \
and is greater than 5".format(number, lastNumber))
elif lastNumber == 0:
    print("Last digit of {:d} is {:d} and is 0\
".format(number, lastNumber))
else:
    print("Last digit of {:d} is {:d} and is less \
than 6 and not 0".format(number, lastNumber))
