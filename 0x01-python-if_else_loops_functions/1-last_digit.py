#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
if number < 0:
    lastNumber = (number * -1) % 10
    flag = 1
else:
    lastNumber = number % 10

if lastNumber > 5:
    print("Last digit of {:d} is {:d} \
and is greater than 5".format(number, lastNumber))
elif lastNumber == 0:
    print("Last digit of {:d} is {:d} and is 0\
    ".format(number, lastNumber))
else:
    if flag == 1:
        print("Last digit of {:d} is {:d} and is less \
than 6 and not 0".format(number, (lastNumber * -1)))
    else:
        print("Last digit of {:d} is {:d} and is less \
than 6 and not 0".format(number, lastNumber))
