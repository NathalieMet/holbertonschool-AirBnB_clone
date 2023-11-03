#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.state import State
from datetime import datetime


class test_state(unittest.TestCase):
    """Test cases for state class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.state = State()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test's environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_save_method(self):
        """Test case for 'save' method"""
        datetime_prev = self.state.updated_at
        self.state.save()
        self.assertGreater(self.state.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.state.__class__.__name__)
        obj_dict = str(self.state.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.state.id, obj_dict)
        self.assertEqual(obj_str, self.state.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.state.id,
            "__class__": self.state.__class__.__name__,
            "created_at": self.state.created_at.isoformat(),
            "updated_at": self.state.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.state.to_dict())


if __name__ == "__main__":
    unittest.main()
