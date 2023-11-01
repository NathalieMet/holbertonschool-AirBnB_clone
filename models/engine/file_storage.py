#!/bin/python3
"""save in storage"""
import json


class FileStorage(BaseException):

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        try:
            if self.__file_path:
                with open(self.__file_path, 'r', encoding='UTF-8') as file:
                    self.__objects = json.load(file)
        except Exception:
            pass
