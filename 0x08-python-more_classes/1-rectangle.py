#!/usr/bin/python3

""" class with getter and setter property """


class Rectangle:
    """ Rectangle class
    Attribute:
        self.__width (int) - private instance width
        self.__height (int) - private instance height
    """
    def __init__(self, width=0, height=0):
        """ automatically initializes object
        Args:
            width (int) - to be assigned to self.__width
            height (int) - to be assigned to self.__height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter method """
        return self.__width

    @property
    def height(self):
        """ getter method """
        return self.__height

    @width.setter
    def width(self, value):
        """ self.__width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("widht must be >= 0")
        self.__height = value

    @height.setter
    def height(self, value):
        """ self.__height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
