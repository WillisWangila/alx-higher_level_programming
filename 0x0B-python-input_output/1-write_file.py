#!/usr/bin/python3

"""
Write string to text file, return no of charaters written
"""


def write_file(filename="", text=""):
    """Writes text to file

    Args:
        filename (str, optional): File to be written to. Defaults to "".
        text (str, optional): Text written to file. Defaults to "".

    Returns:
        int: No. of characters written
    """
    with open(filename, "w") as openfile:
        openfile.write(text)
        count = len(text)
        return count
