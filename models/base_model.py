#!/usr/bin/python3

"""
"""
import uuid
from datetime import datetime
from models import storage
import json

class BaseModel:
    
    def __init__(self,*args,**kwargs):
        if kwargs != None and len(kwargs) > 0:
            for k,v in kwargs.items():
                if k != "__class__":
                    if "ted_at" in k:
                        self.__setattr__(k,datetime.fromisoformat(v))
                    else:
                        self.__setattr__(k,v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
         
                    
    def save(self):
        self.updated_at = datetime.now()
        selfID = f"{self.__class__.__name__}.{self.id}" 
        objs = storage.all()
        if selfID not in objs.keys() :
            storage.new(self.to_dict())
        else:
            storage.update(self.to_dict(), selfID)
        storage.save()
    
    def update(self, atrr,val):
        try:
            val = json.loads(val)
        except: 
            val = val
        self.__setattr__(atrr, val)
    
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
    