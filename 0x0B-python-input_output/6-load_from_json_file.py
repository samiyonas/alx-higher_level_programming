#!/usr/bin/python3

""" write a function to load object from JSON file """
import json


def load_from_json_file(filename):
    """ loads JSON file to our python object """
    with open(filename, 'r', encoding="utf-8") as myfile:
        j = json.load(myfile)
        return j
