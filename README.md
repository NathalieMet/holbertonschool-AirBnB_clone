# Airbnb Clone Console

## Project Description

The Airbnb Clone Console is a command-line interface (CLI) that allows you to interact with a vacation rental management system inspired by Airbnb. You can use this console to create, read, update, and delete objects such as users, reviews, places and more.

## Command Interpreter Description

AirBnB Console is a command-line interface (CLI) that allows you to interact in interactive and non-interactive modes with your AirBnB application. It provides a set of commands to manage instances of various classes, such as BaseModel, and manipulate data.

## How to Get Started

1. Clone the repository from GitHub:
git clone git@github.com:NathalieMet/holbertonschool-AirBnB_clone.git

2. Navigate to the project directory:
cd holbertonschool-AirBnB_clone

3. Run the command interpreter:
./console.py
The command interpreter should now be ready for use.

## How to Use the Command Interpreter
The command interpreter supports various commands and options. Here are some examples of commonly used commands:

Create a new instance of a class:

Usage: create <class name>

Exemple: create User

Show the representation of an instance based on the class name and id:

Usage: show <class name> <instance ID>

Exemple: show BaseModel 1234-1234-1234

Destroy an instance based on the class name and id:

Usage: destroy <class name> <instance ID>

Exemple: destroy Review 1234-1234-1234

Print all string representation of all instances based or not on the class name:
Usage: all [<class name>]
Exemples: all State
		  all

Update an instance based on the class name and id by adding or updating attribute:

Usage: update <class name> <instance ID> <attribute name> "<attribute value>"

Exemple: update Amenity 1234-1234-1234 name "new_name"

After starting the console, you can enter commands as described in the section above. Use the commands to create, show, destroy, list, and update instances of various classes.

## Authors
Cremey Erwan
Metreau Nathalie
For a full list of contributors, please refer to the AUTHORS file.
