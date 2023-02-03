#!/usr/bin/python3
"""Defines a function that prints squares."""


def print_square(size):
    """Prints a square using the # symbol.
    Args:
        size (int): The length of the side of the square.
    Raises:
        TypeError: Raised if size is not an integer.
        ValueError: Raised if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
