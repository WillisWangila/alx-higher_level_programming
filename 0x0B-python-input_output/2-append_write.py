#!/usr/bin/python3

"""
Appends a string at the end of a text file,
returns the no. of characters added
"""


def append_write(filename="", text=""):
    """Writes a string to text file

    Args:
        filename (str, optional): File to be appended/created. Defaults to "".
        text (str, optional): Text to be added to file. Defaults to "".

    Returns:
        int: no. of characters appended to file
    """
    with open(filename, "a") as openfile:
        return openfile.write(text)
