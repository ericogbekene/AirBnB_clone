#!/usr/bin/python3
""" module for the entry point of the console """


import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
    """ class to enter cmd console """

    prompt = '(hbnb)'

    class_dict = {
    'BaseModel': BaseModel,
    'Amenity' : Amenity,
    'City' : City,
    'Place' : Place,
    'Review' : Review,
    'State' : State,
    'User' : User
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
        args = line.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        else:
            objType = args[0]
            if objType in self.class_dict.keys():
                new_instance = self.class_dict[objType]()
                #new_object = objType()
                print('{}'.format(new_instance.id))
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
            
    def do_destroy(self, line):
        """ Method to destroy a class based on ID"""
        args = line.split()
        if len(args) > 0:
            if args[0] in self.class_dict.keys():
                if len(args) == 2 and args[1]:
                    idNum = args[1]
                    for key, value in storage.all().items():
                        id_split = key.split('.')
                        if idNum == id_split[1]:
                            del value
                            storage.save()
                            return
                    print('** no instance found **')
                else:
                    print('** instance id missing **')
            else:
                print("** class doesn't exist **")
        else:
            print('** class name missing **')
        
    def do_all(self, line):
        """ return a print of dictionary representation of all objects"""
        if not line:
            for key, value in storage.all().items():
                print(str(value))
        else:
            args = line.split()
            if args[0] not in self.class_dict.keys():
                print("** class doesn't exist **")
                return
            list_output = []
            """ Create an empty List to hold all strings of BaseModel"""
            for _, value in storage.all().items():
                list_output.append(str(value))
            print(list_output)
            
    def do_update(self, line):
        """ command to update an attribute """
        args = line.split(' ')
        if len(args) != 4:
            if len(args) == 0:
                for i in args:
                    print(i)
                print("** class name missing **")
                return
            elif len(args) == 1:
                print('** instance id missing **')
                return
            elif len(args) == 2:
                print('** attribute name missing **')
                return
            elif len(args) == 3:
                print('** value missing **')
            else:
                print("** class name missing **")
                return
        print(args[0])
        if args[0] in self.class_dict.keys():
            idNum = args[1]
            for key, value in storage.all().items():
                id_split = key.split('.')
                if idNum == id_split[1]:
                    if hasattr(value, args[2]):
                        """check if attribute exists"""
                        try:
                            setattr(value, args[2], args[3])
                            storage.save()
                            return
                        except Exception as e:
                            print('Custom Error here')
                            return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")
            
    """       
    @staticmethod
    def _get_instance_by_id(clsName, idNum):
        instances = [x for x in ObjectTracker._instances if isinstance(x, BaseModel)]
        for obj in instances:
            if type(obj).__name__ == clsName and str(obj.id) == idNum:
    """
            
    @staticmethod
    def count_instances(class_name):
        """ static method to count the number of instances of a class"""
        count = 0
        
        for _, value in storage.all().items():
            if type(value).__name__ == class_name:
                """ check if is an instance of the class and add to count"""
                count += 1
        return count



if __name__ == '__main__':
    HBNBCommand().cmdloop()
