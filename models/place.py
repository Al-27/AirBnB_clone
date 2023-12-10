#!/usr/bin/python3

"""
"""
from models.base_model import BaseModel
import json


class Place(BaseModel):
    """
        Place
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """doc
        """
        super().__init__(**kwargs)
        if kwargs is None and len(kwargs) == 0:
            self.city_id = ""
            self.user_id = ""
            self.name = ""
            self.description = ""
            self.number_rooms = 0
            self.number_bathrooms = 0
            self.max_guest = 0
            self.price_by_night = 0
            self.latitude = 0.0
            self.longitude = 0.0
            self.amenity_ids = []

    def __setattr__(self, attr, val):
        """

        """
        try:
            if attr in [
                    "number_rooms",
                    "number_bathrooms",
                    "max_guest",
                    "price_by_night"] and not isinstance(
                    val,
                    int):
                raise TypeError(f"{attr} must be an integer")
            elif "itude" in attr and not isinstance(val, float):
                raise TypeError(f"{attr} must be a float")
        except Exception as e:
            print(e)
            return
        super().__setattr__(attr, val)

    def update(self, atrr, val):
        """

        """
        try:
            val = json.loads(val)
        except BaseException:
            val = val
        self.__setattr__(atrr, val)
