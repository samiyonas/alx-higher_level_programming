#!/usr/bin/python3

""" Define a Class """


class Square:
    """ A class that calculates area for it's objects

    Attribute:
        __size (int) - validated integer
    """
    def __init__(self, size=0):
        """ __init__ is a method used to initialize it's objects

        Attribute:
            size (int) - to be validated to be assigned to __size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculates the area using __size

        Return:
            returns the area it calculated
        """
        return self.__size * self.__size
