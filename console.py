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

    # Other methods (do_destroy, do_all, do_update) would follow a similar pattern.

if __name__ == '__main__':
    HBNBCommand().cmdloop()
