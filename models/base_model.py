#!/bin/python3
"""Python console"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class for managing data objects"""
    def __init__(self, *args, **kwargs):
        """Initialize an instance of BaseModel.

        Args:
            kwargs (dict): A dictionary containing the instance's attributes.

        Attributes:
            id (str): Unique identifier generated for the instance.
            created_at (datetime): Date and time of instance creation.
            updated_at (datetime): Date and time of
            the last update to the instance.
        """

        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.updated_at = self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance.

        Returns:
            str: A string containing information about the instance.
        """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates the time of the last modification
        of the instance and saves the data."""

        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)

    def to_dict(self):
        """Returns a copy of the instance data in dictionary format.

        Returns:
            dict: A dictionary containing the instance's data.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
