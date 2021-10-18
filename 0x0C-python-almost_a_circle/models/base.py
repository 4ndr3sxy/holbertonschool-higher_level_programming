#!/usr/bin/python3

"""Imports"""
import json

"""Class/Object Base - base code to other class's"""


class Base:
    """No inheritance"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert from python to Json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create file .json and save objects"""
        new_list = []
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as f:
            for i in range(len(list_objs)):
                obj_converted = cls.to_dictionary(list_objs[i])
                new_list.append(obj_converted)
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert from Json to Python object"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance using cls"""
        if cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """Load information of file .json"""
        new_list = []
        filename = str(cls.__name__) + ".json"
        with open(filename, 'r') as f:
            read_line = f.read()
        lists = cls.from_json_string(read_line)
        for i in lists:
            new_list.append(cls.create(**i))
        return new_list
