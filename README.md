# AirBnB clone - The console

<p align="center">
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200702%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200702T055729Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9c4622f8d339618c7e44709c3c8066b8166c741362e2e4adeaef351756002f30.jpg" />
</p>

The goal of the project is to deploy on a server a simple copy of the AirBnB website.
The console is the first stage of the project that consists of:

- Create a data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)
  Manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself). The flow of serialization/deserialization will be:

### Instance <-> Dictionary <-> JSON string <-> file

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
The console will be a tool to validate this storage engine

<p align="center">
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200702%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200702T055729Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2bbf5d26455d6a0beb55d61637a55d7d457df6a389954e597f7a8278f98b168d.jpg" />
</p>

## What's a command interpreter?

A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.

## How to start the console:

To start the console, first clone the repository:

```Python
$ git clone https://github.com/monicajoa/AirBnB_clone.git
```

```bash
$ ./console.py
```

## Usage

It should work like this in interactive mode:

```python3
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
(hbnb)
(hbnb) quit
$
```

And in non-interactive mode:

```python3
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Files

| File Name                     | Description                                                                                                                  |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| console.py                    | Hbnb command interpreter                                                                                                     |
| models/\_\_init\_\_.py        | Contructor for the models Package and create an instance from FilesStorage                                                   |
| models/base_model.py          | Module that holds a class BaseModel that is the main class in the project                                                    |
| models/user.py                | Module that holds User class that inherits from BaseModel                                                                    |
| models/state.py               | Module that holds State class that inherits from BaseModel                                                                   |
| models/city.py                | Module that holds City class that inherits from BaseModel                                                                    |
| models/amenity.py             | Module that holds Amenity class that inherits from BaseModel                                                                 |
| models/place.py               | Module that holds Place class that inherits from BaseModel                                                                   |
| models/engine/\_\_init\_\_.py | Contructor for the engine Package                                                                                            |
| models/engine/file_storage.py | Module that holds the class FileStorage that handle all serialization-deserialization, to a JSON file for a persistent model |
| tests/                        | Module with all the unitest for each .py file                                                                                |

## Commands

| Command | Description                                                                                                              |
| ------- | ------------------------------------------------------------------------------------------------------------------------ |
| EOF     | Exit the program with Ctrl + D                                                                                           |
| all     | Prints all string representation of all instances based or not on the class name.                                        |
| create  | Creates a new instance of Class-Name, saves it (to the JSON file) and prints the id.                                     |
| destroy | Deletes an instance based on the class name and id (save the change into the JSON file).                                 |
| help    | List available commands with "help" or detailed help with "help cmd".                                                    |
| quit    | Command to exit the program                                                                                              |
| show    | Prints the string representation of an instance based on the class name and id.                                          |
| update  | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |

## Example

In the Following example these steps are executed:

- Use the command help that show each command interpreted by the console
- Use the command help with the command that we want to know about in this case create, this display the documentation and the usage of the command
- Use create with the name of a Class - BaseModel, this creates a new instance of this class and displays the Id of the object
- Use show with the name of the class and the id that we want to view, this command only gives information about a specific instance, so it displays all the data about the object associated with the id
- Use create with the name of a Class - User, this creates a new instance of this class and displays the Id of the object
- Use command update to add a new attribute to the instance created before, to do that it needs to specify the class, the id and the name of the attribute with its value, it will add or update a specific field from the instance
- Use command show with the previous instance by its id to view the changes implemented with update

```python3
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) help create
Creates a new instance of Class-Name, saves
        it (to the JSON file) and prints the id
        Usage: create <ClassName>
(hbnb) create BaseModel
41d2807b-7135-4530-901a-bffcd75c550e
(hbnb) show BaseModel 41d2807b-7135-4530-901a-bffcd75c550e
[BaseModel] (41d2807b-7135-4530-901a-bffcd75c550e) {'id': '41d2807b-7135-4530-901a-bffcd75c550e', 'created_at': datetime.datetime(2020, 7, 2, 0, 36, 46, 96038), 'updated_at': datetime.datetime(2020, 7, 2, 0, 36, 46, 96055)}
(hbnb) create User
d584f68a-f048-4f61-b5a9-dd76f5c8b403
(hbnb) update User d584f68a-f048-4f61-b5a9-dd76f5c8b403 name "Holberton"
(hbnb) show User d584f68a-f048-4f61-b5a9-dd76f5c8b403
[User] (d584f68a-f048-4f61-b5a9-dd76f5c8b403) {'id': 'd584f68a-f048-4f61-b5a9-dd76f5c8b403', 'created_at': datetime.datetime(2020, 7, 2, 0, 38, 40, 457280), 'updated_at': datetime.datetime(2020, 7, 2, 0, 39, 10, 374325), 'name': 'Holberton'}
```

## Authors

- Monica Ortiz Alvarez [github: monicajoa][1]
- Nicolas Quinchia Osorio [github: nicolasquinchia][2]

[1]: https://github.com/monicajoa
[2]: https://github.com/nicolasquinchia
