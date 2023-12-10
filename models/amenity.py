#!/usr/bin/python3

"""
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """doc
        """
        super().__init__(**kwargs)
        if kwargs is None and len(kwargs) == 0:
            self.name = ""
