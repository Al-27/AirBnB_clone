#!/usr/bin/python3

"""
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """doc
        """
        super().__init__(**kwargs)
        if kwargs is None and len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
