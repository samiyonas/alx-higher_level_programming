#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    res = []
    for i in a_dictionary:
        if a_dictionary.get(i) == value:
            res.append(i)
    if res:
        for i in res:
            del a_dictionary[i]
    return a_dictionary
