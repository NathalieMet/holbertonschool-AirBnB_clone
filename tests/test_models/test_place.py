#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.place import Place
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from os import getenv


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

        """test nadege solomon"""

    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    """def test_place_in_storage(self):
        place = Place()
        storage.save()
        key = "Place.{}".format(place.id)
        self.assertEqual(key in storage.all(), True)"""

    def test_place_set_and_get_name(self):
        place = Place()
        place.name = "laval"
        self.assertEqual(place.name, "laval")
        place.name = "paris"
        self.assertEqual(place.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(Place, BaseModel))

        """tests Nath"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.place = Place()
        cls.place.city_id = "1234-abcd"
        cls.place.user_id = "4321-dcba"
        cls.place.name = "Death Star"
        cls.place.description = "UNLIMITED POWER!!!!!"
        cls.place.number_rooms = 1000000
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 607360
        cls.place.price_by_night = 10
        cls.place.latitude = 160.0
        cls.place.longitude = 120.0
        cls.place.amenity_ids = ["1324-lksdjkl"]

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.place

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_Place(self):
        """chekcing if amenity have attributes"""
        self.assertTrue('id' in self.place.__dict__)
        self.assertTrue('created_at' in self.place.__dict__)
        self.assertTrue('updated_at' in self.place.__dict__)
        self.assertTrue('city_id' in self.place.__dict__)
        self.assertTrue('user_id' in self.place.__dict__)
        self.assertTrue('name' in self.place.__dict__)
        self.assertTrue('description' in self.place.__dict__)
        self.assertTrue('number_rooms' in self.place.__dict__)
        self.assertTrue('number_bathrooms' in self.place.__dict__)
        self.assertTrue('max_guest' in self.place.__dict__)
        self.assertTrue('price_by_night' in self.place.__dict__)
        self.assertTrue('latitude' in self.place.__dict__)
        self.assertTrue('longitude' in self.place.__dict__)
        self.assertTrue('amenity_ids' in self.place.__dict__)

    def test_is_subclass_Place(self):
        """test if Place is subclass of Basemodel"""
        self.assertTrue(issubclass(self.place.__class__, BaseModel), True)

    def test_attribute_types_Place(self):
        """test attribute type for Place"""
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Place(self):
        """test if the save works"""
        self.place.save()
        self.assertNotEqual(self.place.created_at, self.place.updated_at)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)


if __name__ == "__main__":
    unittest.main()
