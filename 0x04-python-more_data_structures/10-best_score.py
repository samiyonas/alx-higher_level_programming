#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    res = max(a_dictionary.keys())
    return res
