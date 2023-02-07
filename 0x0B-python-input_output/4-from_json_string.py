#!/usr/bin/python3

"""
Returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns json representation of a str object
    """
    return json.loads(my_str)
