#!/usr/bin/python3

""" a function that returns either True or False """


def is_same_class(obj, a_class):
    """ checks if the object belongs to the provided class

    Args:
        obj (instance) - to be checked
        a_class (class) - class to check to
    Returns:
        returns either True or False
    """
    if type(obj) == a_class:
        return True
    return False
