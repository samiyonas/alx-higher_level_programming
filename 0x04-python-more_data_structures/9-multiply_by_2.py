#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i, j in a_dictionary.items():
        new[i] = j * 2
    return new
