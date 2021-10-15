#!/usr/bin/python3

"""Imports"""
import json

"""Class/Object Base - base code to other class's"""


class Base:
    """No inheritance"""
    __nb_objects = 0

    """Constructor"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    """Convert from python to Json"""
    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    """Create file .json and save objects"""
    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w') as f:
            for i in range(len(list_objs)):
                obj_converted = cls.to_dictionary(list_objs[i])
                new_list.append(obj_converted)
            f.write(cls.to_json_string(new_list))

    """Convert from Json to Python object"""
    @staticmethod
    def from_json_string(json_string):
        return json.loads(json_string)

    """Create instance using cls"""
    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Square":
            new_obj = cls(1)
        else:
            new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    """Load information of file .json"""
    @classmethod
    def load_from_file(cls):
        new_list = []
        filename = str(cls.__name__) + ".json"
        with open(filename, 'r') as f:
            read_line = f.read()
        lists = cls.from_json_string(read_line)
        for i in lists:
            new_list.append(cls.create(**i))
        return new_list
