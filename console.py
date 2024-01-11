#!/usr/bin/python3
""" module for the entry point of the console """


import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ class to enter cmd console """

    prompt = '(hbnb)'

    class_dict = {
    'BaseModel': BaseModel,
    'FileStorage' : FileStorage
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
        if args is None:
            print("** class name missing **")
        elif len(args) == 2:
            objType = args[0]
            if objType in self.class_dict.keys():
                new_instance = self.class_dict[objType]()
            #new_object = objType()
            #print("Creating %s named '%s'..." % (objType, objName))
            print('{}'.format(new_instance.id))
            new_instance.save()
        else:
            if args[0] not in self.class_dict.keys():
                raise TypeError("** class doesn't exist **")
        #BaseModel()
                
    def do_show(self, line):
        """ prints the string representation based on ID"""
        args = line.split()
        if args[0] in self.class_dict.keys():
            print_class = self.class_dict[args[0]]
            print('{}'.format(print_class))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
