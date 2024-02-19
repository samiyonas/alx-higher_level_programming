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
