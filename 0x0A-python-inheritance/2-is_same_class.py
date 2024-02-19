#!/usr/bin/python3

""" a function that returns either True or False """


def is_same_class(obj, a_class):
    """ checks if the object belongs to the provided class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
