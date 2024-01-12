#!/usr/bin/python3
""" module for the entry point of the console """


import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ class to enter cmd console """

    prompt = '(hbnb)'

    class_dict = {
    'BaseModel': BaseModel
}


    #def do_help(self, line):
        #""" help method is automatically implemented with docstrings """
        #pass

    def do_quit(self, line):
        """ To quit the console """
        return True
    
    def do_EOF(self, line):
        """ eof method is called when you press Ctrl+D """
        print()
        return True
    
    def do_create(self, line):
        """ Create a new object by type and name """
        print("CREATE")
        args = line.split(' ')
        for i in args:
            print('arg is -> {}'.format(i))
        print('{}'.format(args))
        if len(args) == 0:
            print("** class name missing **")
        else:
            objType = args[0]
            if objType in self.class_dict.keys():
                new_instance = self.class_dict[objType]()
                #new_object = objType()
                print('{}'.format(new_instance))
                new_instance.save()
            else:
                print("** class doesn't exist **")
                
    def do_show(self, line):
        """ prints the string representation based on ID"""
        args = line.split()
        if len(args) > 0:
            if args[0] in self.class_dict.keys():
                if len(args) == 2 and args[1]:
                    idNum = args[1]
                    for key, value in storage.all().items():
                        id_split = key.split('.')
                        if idNum == id_split[1]:
                            print('{}'.format(value))
                            return
                    print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')



if __name__ == '__main__':
    HBNBCommand().cmdloop()
