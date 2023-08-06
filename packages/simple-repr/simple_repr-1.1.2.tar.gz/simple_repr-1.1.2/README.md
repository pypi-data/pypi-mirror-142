# Create string representations of classes
[![Build Status](https://app.travis-ci.com/mr-strawberry66/python-repr-generation.svg?branch=master)](https://app.travis-ci.com/mr-strawberry66/python-repr-generation) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![License](https://img.shields.io/github/license/mr-strawberry66/python-repr-generation)
![Pypi Version](https://img.shields.io/pypi/v/simple-repr)
[![Updates](https://pyup.io/repos/github/mr-strawberry66/python-repr-generation/shield.svg)](https://pyup.io/repos/github/mr-strawberry66/python-repr-generation/)

This module contains a class used to generate `__repr__` methods for your classes. This can be done either by inheriting from the `SimpleRepr` class, or by creating a `__repr__` function, and returing `SimpleRepr.make_repr(self)`

## Using the SimpleRepr class
### Inheritance
The easiest way to use this class is to inherit from it, as this saves you from defining a `__repr__` method altogether.
```py
from simple_repr import SimpleRepr


class User(SimpleRepr):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

user = User('John', 25)
print(user)

>>> User(name='John', age=25)
```

### Defining a function
In case you don't want to inherit from the `SimpleRepr` class, or are already inheriting from another class, you can create a `__repr__` function and return the staticmethod `make_repr` from the module.
```py
from simple_repr import SimpleRepr


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return SimpleRepr.make_repr(self)
        
user = User('John', 25)
print(user)

>>> User(name='John', age=25)
```

## Creating an environment
Create a virtual development environment by using the `virtualenv` Python library. You can install this by executing `pip install virtualenv`. 

To create your environment, type `virtualenv venv --prompt "(your-env) "`. Once created, you can activate it by using `source venv/bin/activate`. Once you are done developing, simply type `deactivate` in your terminal.

## Installation
### Using the library
*   Install this library by running `pip install simple-repr`.
*   Import the library by adding `from simple_repr import SimpleRepr` to your code.

### Developing for this library
*   Install the Python libraries required by running `pip install -r dev-requirements.txt`.
*   Before making any commits, ensure that all [`nox`](https://nox.thea.codes/en/stable/) sessions are passing.

*Please ensure to create your environment before you execute any of the installation commands*
