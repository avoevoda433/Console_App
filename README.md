# Degreesconv
Degreesconv is a console app written in the Python programming language. 
With help this app you can convert temperature values from celsius to fahrenheit and vise versa.
## Table of contents
* [Installation](#installation)
* [Usage](#usage)
* [Uninstallation](#uninstallation)
### Author
[Alexey Voevoda](https://github.com/avoevoda433)

## Installation
[Download](https://github.com/iba-gomel-students/avayavoda-python-be/archive/refs/heads/task_1.zip)
archive. Unpack and install app following commands.
```bash
sudo unzip avayavoda-python-be-task_1.zip
cd avayavoda-python-be-task_1/task_1
sudo python3 setup.py build 
sudo python3 setup.py install
```
## Usage
Format of the command: 
```bash
degreesconv [<command>] [<list of params>]
```
You can run app without arguments and get list of available commands:
```bash
degreeconsv

LIST OF AVAILABLE COMMANDS:
c2f             - Format of the command: degreesconv c2f [values ...]
                - Get additional info about command: degreesconv c2f

f2c             - Format of the command: degreesconv f2c [values ...]
                - Get additional info about command: degreesconv f2c
```
You can get information about the application command 
if you run the application with only the first argument.  
```bash
degreesconv c2f

INFO ABOUT COMMAND:
c2f - convert temperature values from celsius to fahrenheit.
        - Format of the command: degreesconv c2f [values ...]
        - [vaues ...] is numbers separated by space.
```
You can convert temperature values the following way:
#### Example
```bash
degreesconv c2f 14 2.5 -44

RESULT:
Temperature in celsius:         14.0, 2.5, -44.0
Temperature in fahrenheit:      57.2, 36.5, -47.2
```
Temperature values must be a numbers and separated by a space.
## Uninstallation
You can uninstall app following command:
```bash
sudo pip3 uninstall degreesconv
```