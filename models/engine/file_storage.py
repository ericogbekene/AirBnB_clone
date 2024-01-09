#!/usr/bin/python
""" Module to create a persistent file storage system"""


#from models.base_model import BaseModel
import datetime
import json
import uuid

class FileStorage:
    """
    a class that serializes instances to a JSON file and
    deserializes JSON files to instances
    """
    __file_path = str('file.json')
    __objects = {}

    """ Public instance methods"""
    def all(self):
        """ returns the dictionary rep of __objects"""
        return self.__objects
    
    def new(self, obj):
        """ method to set __objects"""
        if isinstance(obj, BaseModel):
            """ check if obj is instance of BaseModel"""
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj
            """ confirm the key/value assignment"""

    def save(self):
        """ save a file to a Json Object"""
        new_objects = {}
        for key, value in self.__objects.items():
            new_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(new_objects, f, default=str)
    
    def reload(self):
        """ deserializes a json file to __objects"""
        if self.__file_path is not None:
            with open(self.__file_path, "r") as f:
                data = json.load(self.__file_path)
                return data