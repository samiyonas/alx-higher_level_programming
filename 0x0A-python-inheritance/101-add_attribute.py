#!/usr/bin/python3

""" a function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, attr, value):
    """ Add a new attribute or raise exception

    Args:
        obj (class instance) - to add new attribute to
        attr (attribute) - new obj attribute
        value (any) - any value
    Returns:
        returns nothing but raises exception on error
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
