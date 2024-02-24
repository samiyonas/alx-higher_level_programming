#!/usr/bin/python3

""" Square class that inherits from Rectangle """
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ create Square based on the previous Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ automatically initializes Square

        Args:
            size (int) - size of the square
            x (int) - x coordinate
            y (int) - y coordinate
            id (int) - identity of the base
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, size):
        """ size setter """
        if type(size) is not int:
            raise TypeError("width must be an integer")
        elif size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def __str__(self):
        """ formatted class object """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
