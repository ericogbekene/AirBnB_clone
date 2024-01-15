# AirBnB clone - The console

![AirBnB](docs/static_files/65f4a1dd9c51265f49d0.png "AirBnB The Console")

## Welcome to our AirBnB clone project in partial fulfillment of the requirements of alx
Please read the [AirBnB concept page](https://intranet.alxswe.com/concepts/66) to better understand what this project intends to do

First step: A command interpreter to manage your **AirBnB objects.**
This is the first step towards building our first full web application: the AirBnB clone.<br>
This first step is very important because this is what we will use to build during this project<br>
with all other following projects: **HTML/CSS templating, database storage, API, front-end integration…**

Each task is linked and will help you to understand, below is a list of things to put in place:

- put in place a parent class (called **BaseModel**) to take care of the initialization, serialization and<br>
deserialization of your future instances
- create a simple flow of ***serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file***
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## What will the command interpreter do?
It will behave exactly the same as the C - Shell but limited to a specific use-case. In our case, we want to be able to<br>
manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

 # HBNB console

This is a simple console for the AirBnB clone project. It allows you to create, show, and delete objects in the database.

## Installation

To install the console, simply clone the AirBnB clone repository and run the following command:

```
pip install -r requirements.txt
```

## Usage

To start the console, simply run the following command:

```
python3 console.py
```

This will open the console and you will be able to start interacting with the database.

## Commands

The console supports the following commands:

* **create**: Creates a new object in the database.
* **show**: Prints the string representation of an object in the database.
* **destroy**: Deletes an object from the database.
* **quit**: Quits the console.

## Creating an object

To create a new object, simply use the `create` command followed by the name of the class and the name of the object. For example, to create a new user, you would use the following command:

```
create User username
```

This will create a new user object with the username `username`.

## Showing an object

To show an object, simply use the `show` command followed by the name of the class and the ID of the object. For example, to show the user with the ID `1`, you would use the following command:

```
show User 1
```

This will print the string representation of the user with the ID `1`.

## Deleting an object

To delete an object, simply use the `destroy` command followed by the name of the class and the ID of the object. For example, to delete the user with the ID `1`, you would use the following command:

```
delete User 1
```

This will delete the user with the ID `1` from the database.

## Quitting the console

To quit the console, simply use the `quit` command.

## Example

Here is an example of how to use the console:

```
(hbnb) create User username
(hbnb) show User 1
(hbnb) delete User 1
(hbnb) quit
```

This will create a new user with the username `username`, show the user with the ID `1`, delete the user with the ID `1`, and then quit the console.

## Conclusion


# Requirements
### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation <br>
(python3 -c 'print(__import__("my_module").my_function.__doc__)' and <br>
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class<br>
or method (the length of it will be verified)
