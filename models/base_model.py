#!/usr/bin/python3

"""
"""
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.updated_at = self.created_at = datetime.now()
        
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        return