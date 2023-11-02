#!/bin/python3
"""A file-based storage system for managing data objects"""
import json


class FileStorage():
    """A file-based storage system to save and retrieve data objects.

    Attributes:
        __file_path (str): The path to the JSON data file.
        __objects (dict): A dictionary to store data objects in memory.
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Retrieve all stored data objects.

        Returns:
            dict: A dictionary containing all stored data objects.
        """
        return self.__objects

    def new(self, obj):
        """Add a data object to the storage.

        Args:
            obj: The data object to be added to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the data objects to the JSON data file."""
        dicto_to_save = {}
        for key, value in self.__objects.items():
            dicto_to_save[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(dicto_to_save, file)

    def reload(self):
        """Reload data objects from the JSON data file."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as file:
                for key, value in json.load(file).items():
                    self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
