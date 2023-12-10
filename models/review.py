#!/usr/bin/python3

"""
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """

    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """doc
        """
        super().__init__(**kwargs)
        if kwargs is None and len(kwargs) == 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
