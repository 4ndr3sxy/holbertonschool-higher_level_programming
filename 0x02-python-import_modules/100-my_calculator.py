#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    countArgs = len(sys.argv[1:])
    if countArgs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    numberOne = int(sys.argv[1])
    numberTwo = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == '+':
        print(add(numberOne, numberTwo))
    elif operator == '-':
        print(sub(numberOne, numberTwo))
    elif operator == '/':
        print(div(numberOne, numberTwo))
    elif operator == '*':
        print(mul(numberOne, numberTwo))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
