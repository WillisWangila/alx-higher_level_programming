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

    def to_json(self):
        return self.__dict__