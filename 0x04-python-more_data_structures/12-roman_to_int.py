#!/usr/bin/python3
def search_letter(a_dictionary, letter):
    for key, value in a_dictionary.items():
        if key == letter:
            return value
    return 0


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    dictionary = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    size = len(roman_string)
    i = sum = number = last_number = 0
    while i < size:
        number = search_letter(dictionary, roman_string[i])
        if i > 0:
            last_number = search_letter(dictionary, roman_string[i - 1])
            if last_number < number:
                number -= (last_number * 2)
        sum += number
        i += 1
    return sum
