#!/usr/bin/python3

class Square:
    """
    Class describing a square
    """

    def __init__(self, size=0):
        """

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        size: int
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
