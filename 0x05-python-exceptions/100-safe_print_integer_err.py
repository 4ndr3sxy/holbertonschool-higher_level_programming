#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    stderr_fileno = sys.stderr
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        stderr_fileno.write("Exception: Unknown format code\
 'd' for object of type 'str'\n")
        return False
