#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.city import City
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from os import getenv


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

    def test_instance_creation(self):
        obj = City()
        self.assertIsInstance(obj, City)

    def test_str_representation(self):
        obj = City()
        obj_str = str(obj)
        self.assertTrue("[City]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = City()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'City')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

        """test nadege&solomon"""

    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    """def test_city_in_storage(self):
        city = City()
        storage.save()
        key = "City.{}".format(city.id)
        self.assertEqual(key in storage.all(), True)"""

    def test_city_set_and_get_name(self):
        city = City()
        city.name = "laval"
        self.assertEqual(city.name, "laval")
        city.name = "paris"
        self.assertEqual(city.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(City, BaseModel))

        """Nath tests"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
