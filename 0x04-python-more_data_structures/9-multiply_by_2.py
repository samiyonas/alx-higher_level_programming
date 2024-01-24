#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i, j in a_dictionary.items():
        a_dictionary[i] = j * 2
    return a_dictionary
