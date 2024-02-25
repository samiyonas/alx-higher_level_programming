#!/usr/bin/python3

""" The base of all other classes """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dictionary to JSON strings """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_str = json.dumps(list_dictionaries)
        return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        """ save JSON string to file """
        filename = cls.__name__ + ".json"
        d_list = [cls.to_dictionary(i) for i in list_objs]
        with open(filename, 'w') as myfile:
            json.dump(d_list, myfile)

    @staticmethod
    def from_json_string(json_string):
        """ from JSON string to python object """
        if json_string is None or len(json_string) == 0:
            return []
        list_obj = json.loads(json_string)
        return list_obj

    @classmethod
    def create(cls, **dictionary):
        """ change dictionary to instance """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
