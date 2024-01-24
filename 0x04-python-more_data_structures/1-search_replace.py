#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = my_list[:]
    for i, j in enumerate(res):
        if j == search:
            res[i] = replace
    return res
