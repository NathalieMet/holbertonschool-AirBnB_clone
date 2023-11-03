#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
import os
from models.user import User
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class test_user(unittest.TestCase):
    """Test cases for user class"""

    @classmethod
    def setUpClass(cls):
        """Class method to open test's environment"""
        cls.user = User()
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
        datetime_prev = self.user.updated_at
        self.user.save()
        self.assertGreater(self.user.updated_at, datetime_prev)
        self.assertTrue(os.path.exists("file.json"))

    def test_str_method(self):
        """Test case for str instance representation"""
        cls_name = str(self.user.__class__.__name__)
        obj_dict = str(self.user.__dict__)
        obj_str = "[{}] ({}) {}".format(cls_name, self.user.id, obj_dict)
        self.assertEqual(obj_str, self.user.__str__())

    def test_to_dict_method(self):
        """Test case for 'to_dict' method"""
        dict = {
            "id": self.user.id,
            "__class__": self.user.__class__.__name__,
            "created_at": self.user.created_at.isoformat(),
            "updated_at": self.user.updated_at.isoformat()
        }
        self.assertDictEqual(dict, self.user.to_dict())

    def test_instance_creation(self):
        obj = User()
        self.assertIsInstance(obj, User)

    def test_str_representation(self):
        obj = User()
        obj_str = str(obj)
        self.assertTrue("[User]" in obj_str)
        self.assertTrue(obj.id in obj_str)

    def test_to_dict_method(self):
        obj = User()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'User')
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)

        """test nana et solo"""

    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    """def test_user_in_storage(self):
        user = User()
        storage.save()
        key = "User.{}".format(user.id)
        self.assertEqual(key in storage.all(), True)"""

    def test_review_set_and_get_name(self):
        user = User()
        user.email = "1"
        user.password = "2"
        user.first_name = "3"
        user.last_name = "4"
        self.assertEqual(user.email, "1")
        self.assertEqual(user.password, "2")
        self.assertEqual(user.first_name, "3")
        self.assertEqual(user.last_name, "4")
        user.email = "5"
        user.password = "6"
        user.first_name = "7"
        user.last_name = "8"
        self.assertEqual(user.email, "5")
        self.assertEqual(user.password, "6")
        self.assertEqual(user.first_name, "7")
        self.assertEqual(user.last_name, "8")

    def test_user_inherits_from(self):
        self.assertTrue(issubclass(User, BaseModel))

        """tests Nath"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kevin"
        cls.user.last_name = "Yook"
        cls.user.email = "yook00627@gmamil.com"
        cls.user.password = "secret"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_attributes_User(self):
        """chekcing if User have attributes"""
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_attribute_types_User(self):
        """test attribute type for User"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save_User(self):
        """test if the save works"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_User(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)


if __name__ == "__main__":
    unittest.main()
