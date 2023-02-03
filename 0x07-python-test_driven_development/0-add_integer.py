#!/usr/bin/python3
"""Defines a funtion that adds 2 numbers"""


def add_integer(a, b=98):
    """
    Checks type of variables and gets the sum of a and b

    Casts float to int before calculating the sum

    Args:
        a (int or float): 1st variable
        b (int, or float optional): 2nd variable. Defaults to 98.

    Raises:
        TypeError: Raised if a is not an int or float
        TypeError: Raised if b is not an int or float

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
