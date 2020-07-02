# AirBnB clone - The console

The goal of the project is to deploy on your server a simple copy of the AirBnB website. The console is the first stage of the project that consists of:

- Create your data model
- Manage (create, update, destroy, etc) objects via a console / command interpreter
- Store and persist objects to a file (JSON file)

## What’s a command interpreter?

A command interpreter is the part of a computer operating system that understands and executes commands that are entered interactively by a human being or from a program. In some operating systems, the command interpreter is called the shell.

## How to start the console:

```bash
$ ./console.py
```

## Usage

It should work like this in interactive mode:

```python
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

```python
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
