#!/usr/bin/python3
"""
Define class rectangle
"""


class Rectangle:
    """
    Class describing a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int, optional):  width of the rectangle. Defaults to 0.
            height (int, optional): height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        self.number_of_instances += 1

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
        Forms rectangle with print_symbol's value according to the given sizes

        Returns:
            str: '#' or print_symbol's value in the shape of the rectangle
        """
        char_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return char_rectangle
        else:
            i = 0
            while i < self.__height:
                char_rectangle += (str(self.print_symbol) * self.__width)
                if i < self.__height - 1:
                    char_rectangle += "\n"
                i += 1
            return char_rectangle

    def __repr__(self):
        """
        return a string representation of the rectangle that would allow us to
        recreate a new instance of the same object if we pass it to eval()


        Returns:
            str: string representation of the rectangle to be passed to eval
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        Deletes an instance of the class and updates counter
        """
        self.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area or rect_1 if equal

        Args:
            rect_1 (class): Instance of the Rectangle class
            rect_2 (class): Instance of the Rectangle class

        Raises:
            TypeError: Raisedif value provided isn't an instance of Rectangle

        Returns:
            class: Largest instance of the Rectangle class or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
