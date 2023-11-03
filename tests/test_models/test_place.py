#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.place import Place
from datetime import datetime


class test_place(unittest.TestCase):
    """Test cases for place class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.place = Place()
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
        datetime_prev = self.place.updated_at
        self.place.save()
        self.assertGreater(self.place.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.place.__class__.__name__)
        obj_dict = str(self.place.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.place.id, obj_dict)
        self.assertEqual(obj_str, self.place.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.place.id,
            "__class__": self.place.__class__.__name__,
            "created_at": self.place.created_at.isoformat(),
            "updated_at": self.place.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.place.to_dict())

    def test_instance_creation(self):
        obj = Place()
        self.assertIsInstance(obj, Place)

    def test_str_representation(self):
        obj = Place()
        obj_str = str(obj)
        self.assertTrue("[Place]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = Place()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)


if __name__ == "__main__":
    unittest.main()
