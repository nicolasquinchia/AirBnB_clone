#!/usr/bin/python3
"""This module is the contructor for the
    models Package and create an instance from
    FilesStorage and reload all information in
    the JSON file
    """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
