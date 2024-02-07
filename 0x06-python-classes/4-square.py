#!/usr/bin/python3

""" Define a Class """


class Square:
    """ A class that calculates area and uses property

    Attribute:
        __size (int) - private instance attribute (validated integer)
    """
    def __init__(self, size=0):
        """ __init__ initializes objects

        Attribute:
            size (int) - will be validated to be assigned to __size
        """
        self.size = size

    @property
    def size(self):
        """ getter method

        Return:
            this method returns __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ calculates area using __size

        Return:
            the method returns the square of __size attribute
        """
        return self.__size * self.__size
