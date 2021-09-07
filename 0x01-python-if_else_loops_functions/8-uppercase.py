def uppercase(str):
    for char in str:
        asC = ord(char)
        print(chr(asC-32) if asC >= 97 and asC <= 122 else char, end='')
    print()
