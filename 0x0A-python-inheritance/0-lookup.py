#!/usr/bin/python3
""" define a function that returns available attrs and methods """


def lookup(obj):
    """ lists all the available attributes and methods of the object """
    return dir(obj)
