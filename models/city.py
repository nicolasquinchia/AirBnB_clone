#!/usr/bin/python3
"""This module holds a class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City
    Args:
        BaseModel ([class]): Parent class
    """
    state_id = ""
    name = ""
