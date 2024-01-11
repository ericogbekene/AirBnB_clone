#!/usr/bin/python3
""" Creating a new User class that inherits from BaseModel"""


from models.base_model import BaseModel

class User(BaseModel):
    """ a new User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""