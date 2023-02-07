#!/usr/bin/python3

"""
Defines a function that returns dictionary description with
simple data structure for JSON serialization
"""
import json


def class_to_json(obj):
    """
    Returns dictionary description for JSON serialization
    """
    return obj.__dict__
