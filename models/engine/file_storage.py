#!/usr/bin/python3

"""

"""

import json
import os
import pathlib

class FileStorage:
    """
    
    """
    __file_path = f"{pathlib.Path(__file__).parent}/../../database/db.json"
    __objects = {}
    ObjKey = "{}.{}"
    
    def __init__(self):
        """
        """
        parentdir = pathlib.Path(__file__).parent
        if not os.path.isdir(os.path.abspath(f"{parentdir}/../../database/")):
            os.mkdir( os.path.abspath(f"{parentdir}/../../database") )
        
        self.__file_path = os.path.abspath(f"{parentdir}/../../database/db.json")
    
    def all(self): 
        """
        """
        return  self.__objects
    
    
    def new(self, obj):
        """
        """
        key = "{}.{}".format(obj["__class__"].strip('"') ,obj["id"].strip('"') )
        self.__objects[ key ] = obj
    
    
    def update(self, obj, id):
        """
        """
        clsID = "{}".format(id)
        self.__objects[ clsID ] = obj
    
    def delete(self, id):
        """
        """
        return self.__objects.pop(id)
    
    def save(self): 
        """
        """
        jsondb = json.dumps(self.__objects)
        f = open(self.__file_path,'w') 
        f.write(jsondb) 
        f.close()  
    
        
    def reload(self):
        """
        """
        if os.path.isfile(self.__file_path) :
            jsondb = "{}"
            with open(self.__file_path,'r') as f:
                jsondb = f.read()
            self.__objects = json.loads(jsondb) if jsondb != "{}" and jsondb.strip() != "" else {}
        else:
            return