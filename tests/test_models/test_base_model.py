#!/usr/bin/python3
"""Test base_model file
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Tests for the BaseModel class
    """

    def test_basemodel_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/base_model.py"])
        self.assertEqual(result.total_errors, 0)
