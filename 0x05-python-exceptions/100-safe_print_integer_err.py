#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    stderr_fileno = sys.stderr
    try:
        print("{:d}".format(value))
        return True
    except Exception as ex:
        stderr_fileno.write("Exception: {}\n".format(ex))
        return False
