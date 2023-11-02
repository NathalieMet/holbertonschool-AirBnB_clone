#!/bin/python3
"""Python console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"


    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Left cmd interpretor"""
        return True

    def emptyline(self):
        print(end='')

    def do_create(self):
        if not BaseModel.__class__.__name__:
            print("** Class name missing **")
        else:
            try:
                FileStorage.new = type(class_name, (object,), {})
                print(f"Created a new class named {class_name}")
            except NameError:
                print(f"** Class '{class_name}' doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
