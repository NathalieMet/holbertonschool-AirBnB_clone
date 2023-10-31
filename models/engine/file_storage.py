#!/bin/python3
"""save in storage"""
import json


class FileStorage:
    def __init__(self):
        self.__file_path = 'models/file.json'
        self.__objects = []

    def all(self):
        return self.__objects

    def new(self, obj):
        obj = self.__class__.__name__.id

    def save(self):
        with open (self.__file_path, 'w', encoding='UTF-8') as file:
            json.dump(self.__objects, file)

    def reload(self):
        if self.__file_path:
            with open (self.__file_path, 'r', encoding='UTF-8') as file:
                loaded_data = json.load(file)
