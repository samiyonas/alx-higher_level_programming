#!/usr/bin/python3

""" Define a class """


class Square:
    """ This class assigns a positive integer to private object attribute

    Attribute:
        __size (int) - verified to be 0 or positive integer
    """
    def __init__(self, size=0):
        """ __init__ method initializes instances

        Attribute:
            size (int) - will be verified to be assigned to __size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
