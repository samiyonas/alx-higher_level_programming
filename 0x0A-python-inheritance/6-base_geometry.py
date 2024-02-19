#!/usr/bin/python3

""" define a class with public instance method """


class BaseGeometry:
    """ class with one method """
    def area(self):
        """ this function just raises an exception """
        raise Exception("area() is not implemented")
