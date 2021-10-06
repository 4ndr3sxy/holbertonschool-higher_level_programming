#!/usr/bin/python3

def init_line_blank(string, position):
    if len(string) > position:
        while string[position] == ' ':
            position += 1
    return position

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    i = init_line_blank(text, i)
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in (".:?"):
            print("\n")
            i = init_line_blank(text, i + 1)
        else:
            i += 1
