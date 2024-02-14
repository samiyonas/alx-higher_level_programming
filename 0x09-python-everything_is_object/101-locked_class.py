#!/usr/bin/python3

""" Locked Class for memory managment """


class LockedClass:
    """ using __slot__ restrict the name of the instance attributes """
    __slots__ = ["first_name"]

    def __init__(self):
        """ initializes instance attributes """
        pass
