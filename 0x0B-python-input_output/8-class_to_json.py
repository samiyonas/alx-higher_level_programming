#!/usr/bin/python3

""" dictionary version of obj suitable for JSON serialization """


def class_to_json(obj):
    """ class to JSON """
    d = obj.__dict__
    return d
