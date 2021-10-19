#!/usr/bin/python3

"""Imports
Class/Object Base - base code to other class's"""
import json
import csv
import os


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
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Create file .json and save objects"""
        new_list = []
        filename = str(cls.__name__) + ".json"
        if list_objs is not None:
            for i in range(len(list_objs)):
                obj_converted = cls.to_dictionary(list_objs[i])
                new_list.append(obj_converted)
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """Convert from Json to Python object"""
        new_list = []
        if json_string is None or len(json_string) == 0:
            return new_list
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
        if not os.path.exists(filename):
            return new_list
        with open(filename, 'r') as f:
            read_line = f.read()
        lists = cls.from_json_string(read_line)
        for i in range(len(lists)):
            new_list.append(cls.create(**lists[i]))
        return new_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """create save file to kind .csv"""
        filename = str(cls.__name__) + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            fields = ['id', 'size', 'x', 'y']

        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = []
                csv_file = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    obj_convert = obj.to_dictionary()
                    new_list.append(csv_file.writerow(obj_convert))

    @classmethod
    def load_from_file_csv(cls):
        """create load method to file .csv"""
        new_list = []
        new_list2 = []
        filename = str(cls.__name__) + ".csv"
        if cls.__name__ == "Rectangle":
            fields = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            fields = ['id', 'size', 'x', 'y']
        with open(filename, mode='r') as f:
            csv_reader = csv.DictReader(f, fieldnames=fields)
            for obj in csv_reader:
                dict_temp = {}
                for key, value in obj.items():
                    dict_temp[key] = int(value)
                new_list.append(dict_temp)
            for i in new_list:
                new_object = cls.create(**i)
                new_list2.append(new_object)
            return new_list2
