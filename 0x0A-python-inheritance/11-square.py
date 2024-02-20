#!/usr/bin/python3

""" New class square inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class that inherits from Rectangle """
    def __init__(self, size):
        """ initializes square class

        Args:
            size (int) - size of a square
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area implementation """
        return self.__size * self.__size

    def __str__(self):
        """ make the object printable """
        return f"[Square] {self.__size}/{self.__size}"
