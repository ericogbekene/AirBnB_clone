#!/usr/bin/python3
""" Test file for BaseModel """


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    class to test the functionality of BaseModel
    """

    def test_init(self):
        """
        create a new base model and check its properties
        """
        test_model = BaseModel()
        """
        check if ID is a string
        """
        self.assertIsInstance(test_model.id, str)
        """
        check if created at is datetime object
        """
        self.assertIsInstance(test_model.created_at, datetime.datetime)
        # check if updated at is datetime obj
        self.assertIsInstance(test_model.updated_at, datetime.datetime)

        # self.assertIsInstance
        # test save method
        # test todict method

    def test_save(self):
        """ test that updated at works properly with save"""
        save_model = BaseModel()
        initial_time = save_model.updated_at
        save_model.save()
        updated_time = save_model.updated_at
        self.assertNotEqual(initial_time, updated_time)

    def test_str(self):
        """
        test that the string representation of the instance prints properly
        """
        new_model = BaseModel()
        str_test = "[BaseModel] ({}) {}"\
            .format(new_model.id, new_model.__dict__)

        self.assertEqual(str_test, str(new_model))

    def test_dict_method(self):
        """
        test that to dict method works properly
        """

    def test_kwargs(self):
        """
        test init method of new instance with **kwargs
        """
        test_dict = {
            "id": "1234-1234-1234-124a",
            "created_at": "2017-09-28T21:05:54.119427",
            "updated_at": "2017-09-28T21:05:54.119572",
            "__class__": "BaseModel"
        }

        model_from_dict = BaseModel(**test_dict)

        self.assertIsInstance(model_from_dict, BaseModel)
        self.assertEqual(model_from_dict.id, test_dict["id"])


if __name__ == '__main__':
    unittest.main()
