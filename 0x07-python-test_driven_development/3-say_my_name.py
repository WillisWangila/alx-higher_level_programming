#!/usr/bin/python3
"""Defines a function that prints out the provided names"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is' followed by first name and optional last name

    Args:
        first_name (str): first name variable
        last_name (str, optional): last name variable. Defaults to "".

    Raises:
        TypeError: _Raised if first_name is not a string
        TypeError: Raised if last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
