#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from os import getenv


class test_review(unittest.TestCase):
    """Test cases for review class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.review = Review()
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
        datetime_prev = self.review.updated_at
        self.review.save()
        self.assertGreater(self.review.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.review.__class__.__name__)
        obj_dict = str(self.review.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.review.id, obj_dict)
        self.assertEqual(obj_str, self.review.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.review.id,
            "__class__": self.review.__class__.__name__,
            "created_at": self.review.created_at.isoformat(),
            "updated_at": self.review.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.review.to_dict())

    def test_instance_creation(self):
        obj = Review()
        self.assertIsInstance(obj, Review)

    def test_str_representation(self):
        obj = Review()
        obj_str = str(obj)
        self.assertTrue("[Review]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = Review()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'Review')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

# test nana et solo

    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    """def test_review_in_storage(self):
        review = Review()
        storage.save()
        key = "Review.{}".format(review.id)
        self.assertEqual(key in storage.all(), True)"""

    def test_review_set_and_get_name(self):
        review = Review()
        review.text = "laval"
        self.assertEqual(review.text, "laval")
        review.text = "paris"
        self.assertEqual(review.text, "paris")

    def test_review_inherits_from(self):
        self.assertTrue(issubclass(Review, BaseModel))

        """tests Nath"""
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "The srongest in the Galaxy"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_review(self):
        """checking if review have attributes"""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_attribute_types_Review(self):
        """test attribute type for Review"""
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', 'DB')
    def test_save_Review(self):
        """test if the save works"""
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
