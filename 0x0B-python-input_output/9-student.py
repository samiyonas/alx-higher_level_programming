#!/usr/bin/python3

""" a class Student that defines a student """


class Student:
    """ class with one public instance method and initialization """
    def __init__(self, first_name, last_name, age):
        """ automatically initializes an object

        Args:
            first_name (str) - first name of student
            last_name (str) - last name of student
            age (int) - age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns obj __dict__ suitable for JSON serialization """
        return self.__dict__
