#!/usr/bin/python3

""" define a class with area and integer validator """


class BaseGeometry:
    """ A cass with two methods """
    def area(self):
        """ raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this functions validates an integer

        Args:
            name (str) - always presumed to be string
            value (int) - number to be validated
        Returns:
            returns nothing but raises an error on error
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ A sub class with private instance attrs

    Args:
        self.__width (int) - width
        self.__height (int) - height
    Return:
        returns nothing
    """
    def __init__(self, width, height):
        """ magic method to initialize the object

        Args:
            width (int) - a width to be validated
            height (int) - a height to be validated
        """
        super().integer_validator(self, width)
        self.__width = width
        super().integer_validator(self, height)
        self.__height = height
