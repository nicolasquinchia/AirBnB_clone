#!/usr/bin/python3
"""Test base_model file
    """

    import unittest
    import os
    import pep8
    from datetime import datetime
    from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """Test Base

    Args:
        unittest ([test]):
    """
    def test_pep8_style(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0)
