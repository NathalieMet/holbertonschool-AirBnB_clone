#!/bin/python3
"""Python console"""
import uuid
from datetime import datetime


class BaseModel:

    """class Basemodel"""

    def __init__(self):
        """initialize instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print instances"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the time of the last instance"""
        self.updated_at = datetime.now()
        self.updated_at.isoformat()

    def to_dict(self):
        """do a copy of dictionnary"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['update_at'] = self.updated_at.isoformat()
        obj_dict['created_at'] = self.created_at.isoformat()
        return obj_dict
