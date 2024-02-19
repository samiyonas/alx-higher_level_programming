#!/usr/bin/python3

""" define a function that checks for instance """


def is_kind_of_class(obj, a_class):
    """ checks if the object kind of belong to the class

    Args:
        obj - object to be checked
        a_class - a class to match the object to
    Returns:
        returns either True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
