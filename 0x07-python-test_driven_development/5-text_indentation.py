#!/usr/bin/python3
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_string = text.replace(": ", ":\n\n")
    new_string = new_string.replace(". ", ".\n\n")
    new_string = new_string.replace("? ", "?\n\n")
    print(new_string, end='')
