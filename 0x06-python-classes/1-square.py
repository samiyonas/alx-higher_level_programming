#!/usr/bin/python3

""" Define a class with a private instance attribute """


class Square:
    """ A class definition with initializer.

    Attribute:
        __size - private attribute with no type or value verification
    """
    def __init__(self, size):
        """ __init__ is a method that automatically initializes objexts

        Attribute:
            size - no type or value verification
        """
        self.__size = size
