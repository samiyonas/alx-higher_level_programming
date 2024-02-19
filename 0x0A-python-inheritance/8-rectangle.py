#!/usr/bin/python3

""" define a class with area and integer validator """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
