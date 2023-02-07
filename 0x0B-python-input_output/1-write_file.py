#!/usr/bin/python3

"""
Write string to text file, return no of charaters written
"""


def write_file(filename="", text=""):
    with open(filename, "w") as openfile:
        openfile.write(text)
        count = len(text)
        return count
