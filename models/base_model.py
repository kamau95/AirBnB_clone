#!/usr/bin/python3
"""This file holds  the basemodel
class which is the parent class"""

import uuid
from datetime import datetime


class BaseModel:
    """my parent class - other classes will inherit"""
    time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):

        """Initializes instance attributes
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], time_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], time_format)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation"""

        return f"[{self.__class__.__name__}] \
               ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
