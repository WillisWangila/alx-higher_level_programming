#!/usr/bin/python3
"""
Define class rectangle
"""


class Rectangle:
    """
    Class describing a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int, optional):  width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the value of width

        Returns:
        int: width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width

        Args:
            value (int): Value assigned to width by user

        Raises:
            TypeError: Raises error if value provided isn't int
            ValueError: Raises error if value provided is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Retrieves the value of height

        Returns:
            int: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height

        Args:
            value (int): Value assigned to height by user

        Raises:
            TypeError: Raises error if value provided isn't int
            ValueError: Raises error if value provided is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
