#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.city import City
from datetime import datetime


class test_city(unittest.TestCase):
    """Test cases for city class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.city = City()
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
        datetime_prev = self.city.updated_at
        self.city.save()
        self.assertGreater(self.city.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.city.__class__.__name__)
        obj_dict = str(self.city.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.city.id, obj_dict)
        self.assertEqual(obj_str, self.city.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.city.id,
            "__class__": self.city.__class__.__name__,
            "created_at": self.city.created_at.isoformat(),
            "updated_at": self.city.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.city.to_dict())


if __name__ == "__main__":
    unittest.main()
