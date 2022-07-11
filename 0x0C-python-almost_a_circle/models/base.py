#!/usr/bin/python3
"""Base class."""

import json
import os


class Base:
    """Represents the base class.

    Observation:
        The class is used to manage id attribute
        in all your future classes and to avoid duplicating
        the same code (by extension, same bugs)

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate the id class with.

        Args:
            id(int): the class id

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1

            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries(list): list of dictionary

        """
        if list_dictionaries is None or list_dictionaries is " ":
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            with open(cls.__name__+".json", mode = "w") as myfile:
                myfile.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))
    
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string
        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins
