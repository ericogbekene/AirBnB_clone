#!/usr/bin/python3
""" Module to test file storage works properly"""


from models import storage
from models.base_model import BaseModel
import unittest

class TestStorage(unittest.TestCase):
    """ class to test methods and classes of file storage"""
    
    def test_all(self):
        """ test that all returns a dictionary of all saved instances"""
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        
    def test_save(self):
        """ test that save method works correctly"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()
        self.assertEqual(my_model.name, "My_First_Model")
        self.assertEqual(my_model.my_number, 89)
        # print(my_model)
        
        
if __name__ == '__main__':
    unittest.main()
