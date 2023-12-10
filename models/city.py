#!/usr/bin/python3

"""
"""
import uuid
from models.base_model import BaseModel


class City(BaseModel):
    """
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """doc
        """
        super().__init__(**kwargs)
        if kwargs is None and len(kwargs) == 0:
            self.state_id = ""
            self.name = ""
