#!/usr/bin/python3

""" The base of all other classes """


class Base:
    """ the goal is to keep track of id attribute

    Attributes:
        __nb_objects (int) - given to self.id if id is None
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ automatically initializes the base class

        Args:
            id (int) - identity of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
