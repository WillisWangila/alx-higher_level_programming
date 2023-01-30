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

    def area(self):
        """
        Calculates area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculates perimeter of a rectangle

        Returns:
            _type_: _description_
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """
        Method that forms a rectangle of # according to the given sizes

        Returns:
            str: '#' in the shape of the rectangle
        """
        char_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return char_rectangle
        else:
            i = 0
            while i < self.__height:
                char_rectangle += ("#" * self.__width)
                if i < self.__height -1:
                    char_rectangle += "\n"
                i += 1
            return char_rectangle


my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))