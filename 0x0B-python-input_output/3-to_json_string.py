#!/usr/bin/python3

import json

""" a function that changes objects to JSON strings """


def to_json_string(my_obj):
    """ turns object to JSON string and return it """
    json_s = json.dumps(my_obj)
    return json_s
