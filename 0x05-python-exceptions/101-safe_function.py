#!/usr/bin/python3
import sys
stderr_fileno = sys.stderr


def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])
        return result
    except Exception as ex:
        stderr_fileno.write("Exception: {}\n".format(ex))
        return None
