#!/usr/bin/python3

"""
Defines a function that creates an object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    creates an object from JSON file
    Args:
        filename (json): file used to create the object
    """
    with open(filename) as openfile:
        json.load(openfile)
