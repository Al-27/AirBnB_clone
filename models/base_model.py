#!/usr/bin/python3

"""
"""
import uuid
from datetime import datetime

class BaseModel:
    
    def __init__(self,*args,**kwargs):
        if kwargs != None and len(kwargs) > 0:
            for k,v in kwargs.items():
                if k != "__class__":
                    if k.__contains__("ted_at"):
                        self.__setattr__(k,datetime.fromisoformat(v))
                    else:    
                        self.__setattr__(k,v)
                
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
                    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dict = {}
        dict['__class__'] = self.__class__.__name__
        
        for k,v in self.__dict__.items():
            if "ted_at" in k:
                dict[k] = v.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                dict[k] = v
        
        return dict
         
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"