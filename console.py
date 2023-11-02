#!/bin/python3
"""Python console"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
