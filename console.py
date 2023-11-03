#!/bin/python3
"""Python console"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ hbnb command interpreter """
    prompt = "(hbnb)"


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self):
        """Left cmd interpretor"""
        return True

    def emptyline(self):
        print(end='')

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not args:
            print("** class name missing **")
            return
        class_name = args.strip()
        if class_name == "BaseModel":
            new_instance = BaseModel(class_name)
            new_instance.save()
            print(new_instance.id)
        else:
            print(f"** class '{class_name}' doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on class name and id."""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        id_model = args[1]
        if class_name == "BaseModel":
            instance_key = "{}.{}".format(class_name, id_model)
            if instance_key in storage.all():
                instance = storage.all()[instance_key]
                print(instance)
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and ID (save the change into the JSON file)."""
        args = args.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        id_model = args[1]

        if class_name == "BaseModel":
            instance_key = "{}.{}".format(class_name, id_model)
            if instance_key in storage.all():
                del storage.all()[instance_key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):

        list_instance = []
        if not args:
            for instance in storage.all().values():
                list_instance.append(instance.__str__())
            print(list_instance)
        else:
            args = args.split()
            class_name = args[0]
            if class_name == "BaseModel":
                for instance in storage.all().values():
                    list_instance.append(instance.__str__())
                print(list_instance)
            else:
                print("** class doesn't exist **")
       
if __name__ == '__main__':
    HBNBCommand().cmdloop()
