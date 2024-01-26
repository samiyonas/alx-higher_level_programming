#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    l = len(roman_string)
    res = 0
    while i < l:
        if i < l - 1 and rome_dict[roman_string[i]] < rome_dict[roman_string[i + 1]]:
            res -= rome_dict[roman_string[i]]
        else:
            res += rome_dict[roman_string[i]]
        i += 1
    return res
