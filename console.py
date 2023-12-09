#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel 

import cmd

classes =  ["BaseModel", "User", "Place","City"]

def GetClass(classname):
    import importlib
    module = importlib.import_module(f"models.{'base_model' if classname == 'BaseModel' else classname.lower()}")
    ModelClass = getattr(module, classname)
    return ModelClass


def check_invalid(str,id=False, attr=False):
    
    try:
        if len(str) == 0:
            raise TypeError()
    except Exception as e:
        print("** class name missing **")
        return False
    
    try:
        clsn = str[0]
        if clsn == "" or clsn not in classes:
            raise TypeError()
    except Exception as e:
        print("** class doesn't exist **")
        return False
    
    if id:
        try:
            id_ = str[1].strip()
            if id_ == "" :
                raise TypeError()
        except Exception as e:
            print("** instance id missing **")
            return False
    
    if attr:
        try:
            attribute = str[2].strip()
            
            dummy = GetClass(str[0])()
            
            if attribute == "" or not hasattr(dummy,attribute):
                raise TypeError()
        except Exception as e:
            print("** attribute name missing **")
            return False
        
        try:
            val = str[3].strip()
            
            if val == "":
                raise ValueError()
        except Exception as e:
            print("** value missing **")
            return False
        
    return True

def check_instance_exists(id):
    Objs = storage.all()
    
    try:
        classm = Objs[id]
    except Exception as e:
        print( "** no instance found **" )
        return False
    
    return classm
    

class HBNBCommand(cmd.Cmd):
    cmd.Cmd.prompt = "(hbh)"
    
    obj = [BaseModel()]
    def cmdloop(self):
        super().cmdloop()
    
    
    def do_EOF(self, arg):
        print("")
        return True
        
    def do_quit(self, arg):
        return True
    
    def do_create(self, arg):
        arg = arg.strip()
        
        args = arg.split(" ")
        if not check_invalid(args):
            return False
        
        ModelClass = GetClass(args[0])
        mclass = ModelClass()
        print(mclass.id)
        mclass.save()        

    
    def do_show(self, arg):
        arg = arg.strip()
            
        args = arg.split(" ")
        if not check_invalid(args,True) :
            return False
        
        ModelClass = GetClass(args[0])
        classID = f"{args[0]}.{args[1]}"
        obj = check_instance_exists(classID)
        if obj == False :
            return False
        
        mclass = ModelClass(**obj)
        print(mclass)
        
    def do_all(self, arg):
        arg = arg.strip()
            
        args = arg.split(" ")
        if not check_invalid(args) :
            return False
        Bclass = GetClass(args[0])
        strings = []
        for k,v in storage.all().items():
            if args[0] in k:
                bcls = Bclass(**v)
                strings.append( str(bcls) )
        print(strings)
            
    def do_update(self, arg):
        arg = arg.strip()
            
        args = arg.split(" ")
        if not check_invalid(args,True,True) :
            return False
        
        classID = f"{args[0]}.{args[1]}"
        obj = check_instance_exists(classID)
        if obj == False :
            return False
            
        object = storage.all()[classID]
        BClass = GetClass(args[0])
        bclass = BClass(**object)
        bclass.update(args[2],args[3])
        bclass.save()
    
    def do_destroy(self, arg):
        arg = arg.strip()
            
        args = arg.split(" ")
        if not check_invalid(args,True) :
            return False
            
        classID = f"{args[0]}.{args[1]}"
        
        obj = check_instance_exists(classID)
        if obj == False :
            return False
        
        storage.delete(classID)
        storage.save()    
    
        
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()