#!/bin/python3
"""Python console"""
from models.base_model import BaseModel


class User(BaseModel):
    """Create instance of user
        Attributes:
            email, password, first_name, last_name
        """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
