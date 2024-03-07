"""
this file contains a base class BaseModel that
defines all common attributes/methods for other classes
"""


import uuid
import datetime


class BaseModel:
    """this is base class"""
    time_format = '%Y-%m-%dT%H:%M:%S.%f'

    def __init__(self, *args, **kwargs):
        """initialization of a new BaseModel instance"""
        if kwargs:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    value = datetime.datetime.strptime(value, self.time_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def save(self):
        """updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """adding new key/value pairs to my object"""
        obj_dict = self.__dict__.copy()

        """Convert created_at and updated_at to ISO format strings"""
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        """Add __class__ key with the value class name"""
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """overwriting the str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
