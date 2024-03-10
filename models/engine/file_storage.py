import json


"""this module handles the creation of an \
        instance, saving it ser-desrializing it"""


class FileStorage:
    """this class serializes instances to a JSON file \
    and deserializes JSON file to instances"""
    def __init__(self, file_path, objects={}):
        """constructor of the filestorage"""
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """returns all the objects"""
        return self.__objects

    def new(self, obj):
        """adds a new object obj to a dictionary using key classname.id"""
        """setting obj inside a dict by using above key"""

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """save method serializes the objects\
                and writes them to the file."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """this reads and decodes objects from a JSON file,\
                creating instances of the corresponding classes \
                and adding them to the __objects dictionary"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
            for key, obj_data in loaded_objects.items():
                class_name, object_id = key.split(".")
                obj_class = eval(class_name)
                obj_instance = obj_class(**obj_data)
                self.__objects[key] = obj_instance

        except FileNotFoundError:
            pass

from models.base_model import BaseModel
