#!/usr/bin/python3
"""doc
"""
from models import storage
from models.base_model import BaseModel

import cmd
import re
import json

classes = ["BaseModel", "User", "Place", "City", "Amenity", "Review", "State"]


def GetClass(classname):
    """
    return the Class of the specified classname from the module
    """
    import importlib
    module = importlib.import_module(
        f"models.{'base_model' if classname == 'BaseModel' else classname.lower()}")
    ModelClass = getattr(module, classname)
    return ModelClass


def splitstr(str):
    """
        properly strip a string that has quotes into a string
    """
    lst = []
    isjoin = False
    joined = []

    for i in str.split():
        if '"' in i or isjoin:
            joined.append(i)

        if i[0] == '"' and i[-1] == '"' and not isjoin:
            newstr = " ".join(joined)
            lst.append(newstr.strip('" '))
        elif i[0] == '"' and not isjoin:
            isjoin = True
        elif i[-1] == '"':
            isjoin = False
            newstr = " ".join(joined)
            lst.append(newstr.strip('" '))
        elif not isjoin:
            lst.append(i)

    return lst


def check_invalid(str, id=False, attr=False):
    """
        pass a list of commands(str) then check if
        class name valid
        class exists
        if @id is true then check if user passed an id and the instance with id exists
        if @attr is true then check if user passed attribute name&value and if each of the two is valid
    """
    try:
        if len(str) == 0 or str[0] == '':
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
            if id_ == "":
                raise TypeError()
        except Exception as e:
            print("** instance id missing **")
            return False

    if attr:
        try:
            attribute = str[2].strip()

            dummy = GetClass(str[0])()

            if attribute == "":  # or not hasattr(dummy,attribute):
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
    """
    check if @id exists in the database
    """
    Objs = storage.all()

    try:
        classm = Objs[id]
    except Exception as e:
        print("** no instance found **")
        return False

    return classm


class HBNBCommand(cmd.Cmd):
    """
    the console
    """
    cmd.Cmd.prompt = "(hbnb)"

    def cmdloop(self):
        """
        """
        super().cmdloop()

    def emptyline(self):
        return

    def onecmd(self, line):
        # func (?<=\.).*(?=\(\))
        # class .*(?=\.)
        # args (?<=\().*(?=\))
        if re.match(r"\w+\.\w+\((.*|)\)", line) is None:
            return super().onecmd(line)
        else:
            func = re.search(r"(?<=\.).*(?=\(.*\))", line)[0]
            classname = re.search(r"\w*(?=\..*\()", line)
            classname = "" if classname is None else classname[0]
            args = re.search(r"(?<=\().*(?=\))", line)
            args = "" if args is None else args[0]

            if func == "count":
                count = 0
                for k in storage.all().keys():
                    if classname in k:
                        count += 1
                print(count)
            elif func == "update":
                try:
                    id = args.split(",", 1)[0]
                    dic = json.loads(args.split(",", 1)[1])

                    for attr, val in dic.items():
                        command = f'{func} {classname} {id} {attr} {val}'
                        super().onecmd(command)
                except Exception as e:
                    argsl = args.split(",")
                    while len(argsl) < 3:
                        argsl.append("")
                    command = f'{func} {classname} {argsl[0]} {argsl[1]} {args[2]}'
                    super().onecmd(command)
            else:
                command = f"{func} {classname} {args}"
                super().onecmd(command)

    def do_EOF(self, arg):
        """
        EOF
            exit the console, ctrl+D or simply type EOF.
        """
        return True

    def do_quit(self, arg):
        """
        quit
            exit the console.
        """
        return True

    def do_create(self, arg):
        """
        create
            create a new instance of type <class name>:
                create <class name>
        """
        arg = arg.strip()

        args = splitstr(arg)
        if not check_invalid(args):
            return False

        ModelClass = GetClass(args[0])
        mclass = ModelClass()
        print(mclass.id)
        mclass.save()

    def do_show(self, arg):
        """
        show
            prints <class name>'s instance with the passed <id> (if it exists):
            show <class name> <id>
        """
        arg = arg.strip()
        args = splitstr(arg)
        if not check_invalid(args, True):
            return False

        ModelClass = GetClass(args[0])
        classID = f"{args[0]}.{args[1]}"
        obj = check_instance_exists(classID)
        if not obj:
            return False

        mclass = ModelClass(**obj)
        print(mclass)

    def do_all(self, arg):
        """
        all
            prints all instances in the database, or those of type of <class name> ([] indicates argument is optional):
            all [<class name>]
        """
        arg = arg.strip()

        args = splitstr(arg)
        if len(args) != 0:
            if not check_invalid(args):
                return False
        strings = []
        for k, v in storage.all().items():
            if len(args) != 0:
                Bclass = GetClass(args[0])
                if args[0] in k:
                    bcls = Bclass(**v)
                    strings.append(str(bcls))
            else:
                Bclass = GetClass(v["__class__"])
                bcls = Bclass(**v)
                strings.append(str(bcls))
        print(strings)

    def do_update(self, arg):
        """
        update
            update an instance attribute:
            update <class name> <id> <attribute name> "<attribute value>"
                !: use quotation marks if attribute value has spaces in it
        """
        arg = arg.strip()

        args = splitstr(arg)
        if not check_invalid(args, True, True):
            return False

        classID = f"{args[0]}.{args[1]}"
        obj = check_instance_exists(classID)
        if not obj:
            return False

        object = storage.all()[classID]
        BClass = GetClass(args[0])
        bclass = BClass(**object)
        bclass.update(args[2], args[3])
        bclass.save()

    def do_destroy(self, arg):
        """
        destroy
            destroy an instance:
            destroy <class name> <id>
        """
        arg = arg.strip()

        args = splitstr(arg)
        if not check_invalid(args, True):
            return False

        classID = f"{args[0]}.{args[1]}"

        obj = check_instance_exists(classID)
        if not obj:
            return False

        storage.delete(classID)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
