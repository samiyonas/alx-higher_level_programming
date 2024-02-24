#!/usr/bin/python3

""" Rectangle class that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ create Rectangle class

    Attributes:
        __width (int) - width of rectangle
        __height (int) - height of Rectangle
        __x (any) - will document later
        __y (any) - will document later
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ automatically initializes Rectangle objects

        Args:
            width (int) - width of rectangle
            height (int) - height of rectangle
            x (any) - will document later
            y (any) - will document later
            id (int) - identity of the base
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
