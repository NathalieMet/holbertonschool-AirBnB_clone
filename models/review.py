#!/bin/python3
"""Python console"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Create instance of place
        Attribute:
            user_id, place_id, text
        """
    place_id = ""
    user_id = ""
    text = ""
