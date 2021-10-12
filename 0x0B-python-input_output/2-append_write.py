def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        count_chars = f.write(text)
    return count_chars
