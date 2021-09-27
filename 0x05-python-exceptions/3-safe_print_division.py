#!/usr/bin/python3
def safe_print_division(a, b):
    validate = False
    try:
        result = a / b
    except:
        validate = True
    finally:
        return result if not validate else None
