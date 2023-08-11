#!/usr/bin/python3
""" ALX AirBnB Console """
import cmd
import sys
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    def do_quit(self, arg):
        """ Exit method for quitting """
        sys.exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        sys.exit()

    def emptyline(self):
        """ Method to pass when empty line is entered """
        pass

    def get_instance(self, class_name, instance_id):
        """ Retrieve an instance based on class name and ID """
        key = "{}.{}".format(class_name, insance_id)
        instance = storage.all().get(key)
        if instance:
            return instance
        else:
            print("** no instance found **")

    def do_create(self, arg):
        """ Create a new instance """
        if not arg:
            print('** class name missing **')
            return

        class_name = arg.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Display instance details """
        if not arg:
            print('** class name missing **')
            return

        class_name, instance_id = arg.split()[0], arg.split()[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.get_instance(class_name, instance_id)
        if instance:
            print(instance)

    def do_all(self, arg):
        """ Method to print all instances """
        if len(arg) == 0:
            print([str(a) for a in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(a) for b, a in storage.all().items() if arg in b])
    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print('** instance id missing **')
            return
        if len(arg_list) > 1:
            key = arg_list[0] + '.' + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print('** no instance found **')
                return
    def do_update(self, arg):
        """ Method to update JSON file"""
        arg = arg.split()
        if len(arg) == 0:
            print('** class name missing **')
            return
        elif arg[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print('** instance id missing **')
            return
        else:
            key = arg[0] + '.' + arg[1]
            if key in storage.all():
                if len(arg) > 2:
                    if len(arg) == 3:
                        print('** value missing **')
                    else:
                        setattr(
                            storage.all()[key],
                            arg[2],
                            arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print('** attribute name missing **')
            else:
                print('** no instance found **')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
