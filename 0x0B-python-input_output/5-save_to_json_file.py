#!/usr/bin/python3

"""
Defines function that writes an object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    """
    with open(filename, "w") as openfile:
        json.dump(my_obj, openfile)
