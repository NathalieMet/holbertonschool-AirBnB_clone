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
        self.__objects.dump

    def reload(self):


