#!/usr/bin/python3

""" write object to a text file using JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ saves an object to JSON file """
    with open(filename, 'w', encoding="utf-8") as myfile:
        json.dump(my_obj, myfile)
