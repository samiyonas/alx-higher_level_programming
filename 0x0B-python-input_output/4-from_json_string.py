#!/usr/bin/python3

""" a function that changes JSON strings to python objects """
import json


def from_json_string(my_str):
    """ turns JSON string to python object and return it """
    my_obj = json.loads(my_str)
    return my_obj
