#!/usr/bin/python3
""" Base model for all instanes of objects """
import uuid
import datetime
from models import storage


class BaseModel:
    """
    class to define all commmon attributes and methods for all classes
    """

    """ Public instance attributes """
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Overiding string representation of object to print desired output
        """
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """ Public instance method to update attribute updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary repr of all key/value pairs of an object
        """
        obj_dict = {k: v for k, v in self.__dict__.items()}
        obj_dict['__class__'] = self.__class__.__name__
        if hasattr(self, 'created_at') and isinstance(self.created_at, datetime.datetime):
            obj_dict['created_at'] = self.created_at.isoformat()
        """ should this use strftime instead ??"""
        if hasattr(self, 'updated_at') and isinstance(self.created_at, datetime.datetime):
            obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
    def __init__(self, *args, **kwargs):
        """ Generate an instance from a dictionary representation"""
        if kwargs:
            for key, value in kwargs.items():
                if key not in ['__class__']:
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            #super().__init__(*args)
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self)