def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        count_chars = f.write(text)
    return count_chars
