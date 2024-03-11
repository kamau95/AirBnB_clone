import uuid
from datetime import datetime


"""
this file will hold the parent class
"""


class BaseModel:
    """
    this class defines the common
    attributes and mthds of child classes
    """
    def __init__(self, *args, **kwargs):
        """This method initializes a new BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"
                    )
                    setattr(self, key, value)

    def save(self):
        """
        updates the updated_at attribute
        with the current datetime
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """
        returns a string representation
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

    def to_dict(self):
        """
        This method returns a dictionary
        representation of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
