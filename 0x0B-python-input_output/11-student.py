#!/usr/bin/python3

"""
Defines a Student class
"""


class Student:
    """
    Represents a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student

        Args:
            first_name (str): Student's first name
            last_name (str): Student's lasst name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of an instance of Student

        Args:
            attrs (list, optional): Instance attributes. Defaults to None.

        Returns:
            dict: instance attributes as keys and given values as values
        """
        a = {}
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            # return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
            for i in attrs:
                if hasattr(self, i):
                    a[i] = getattr(self, i)
            return a
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        Uses the key/value pairs in the json dictionary for the replacement

        Args:
            json (dict): contains the key/value pairs
        """
        for key, value in json.items():
            setattr(self, key, value)
