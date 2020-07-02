#!/usr/bin/python3
"""This module holds a class BaseModel
    that is the main class in the project
    """
import uuid
import datetime
from models import storage


class BaseModel:
    """BaseModel main class set the value of a
    new instance or instance a class from a
    dictionary of an object previous created
    """

    def __init__(self, *args, **kwargs):
        """Constructor method that initilize an
        instance o create a new one from a
        dictionary in the paramether kwargs
        """
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id = str(uuid.uuid4())
            if "craeted_at" in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                self.created_at = datetime.datetime.now()
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                self.updated_at = datetime.datetime.now()
            for key, value in kwargs.items():
                if key in ["id", "created_at", "updated_at", "__class__"]:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """No official representation of an object
        Returns:
            [str]: Representation No Oficial of the instance
        """
        printable_str = "[{}] ({}) {}".format(
            type(self).__name__, self.id, str(self.__dict__)
        )
        return printable_str

    def save(self):
        """Public Instance Method that update
        the datetime and storage the instance
        serializating and saving in a JSON file
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Public Instance Method that create a
        dictionary with all the information of
        the instance with a spaceific format
        Returns:
            [dic]: Dictionary with all instance information
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        return new_dict
