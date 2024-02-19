#!/usr/bin/python3

""" define a function to check inherited classes """


def inherits_from(obj, a_class):
    """ check for inherited classes

    Args:
        obj - to be checked
        a_class - a class to match the type of the object to
    Returns:
        returns either True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
