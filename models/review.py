#!/usr/bin/python3
"""This module holds a class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review
    Args:
        BaseModel ([class]): Parent class
    """
    place_id = ""
    user_id = ""
    text = ""
