#!/bin/python3
"""Python console"""
from models.base_model import BaseModel


class City(BaseModel):
    """Create instance of city
        Attributes:
            state_id, name
        """
    state_id = ""
    name = ""
