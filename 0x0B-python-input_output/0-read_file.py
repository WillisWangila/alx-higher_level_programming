#!/usr/bin/python3
"""
Reads a text file and prints to stdout
"""

def read_file(filename=""):
    """Opens file and prints content

    Args:
        filename (str, optional): Filename. Defaults to "".
    """
    with open(filename, encoding="utf-8") as openfile:
        print(openfile.read(), end="")
