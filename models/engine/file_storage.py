#!/bin/python3
"""save in storage"""
import json
import os


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open (self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(serialized, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open (self.__file_path, 'r', encoding='UTF-8') as file:
                try:
                    data = json.load(file)
                    for key, value in data.items():
                        class_name, obj_id = key.split(".")
                        cls = models[class_name]
                        self.__objects[key] = cls(**value)
                except Exception:
                    pass


models = {
    "BaseModel": BaseModel
}
