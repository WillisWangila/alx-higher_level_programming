#!/usr/bin/python3
"""
Define class square
"""


class Square:
    """
    Class describing a square
    """

    def __init__(self, size):
        """
        Initialize a new square

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size
