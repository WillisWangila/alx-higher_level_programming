#!/usr/bin/python3

class Square:
    """
    Class describing a square
    """
    def __init__(self, size=0):
        """

        Args:
            size (int, optional): Size of the square's sides. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the value of size

        Returns:
            int: Value of 'size' variable
        """
        return self.__size

    # 1. The first line of the setter method definition is decorator @size.setter.
    # 2. The decorator creates and returns a setter method for attribute size.
    # 3. The setter method takes one argument, value.
    # 4. The setter method checks if the value is an integer.
    # 5. The setter method checks if the value is greater than or equal to 0.
    # 6. If the value is an integer and greater than or equal to 0, the setter method assigns the value to the attribute size.
    # 7. If the value is not an integer or is less than 0, the setter method raises an error.
    @size.setter
    def size(self, value):
        """Sets the value of size

        Args:
            value (int): Integer provided by user assigned as value to 'size'

        Raises:
            TypeError: Raises error if value provided isn't int
            ValueError: Raises error if value provided is less than 0
        """
        value: int
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square

        Returns:
            int: Area of the square
        """
        side = self.__size
        squared = side * side
        return squared

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        side = self.__size
        for i in range(side):
            for i in range(side):
                if (side == 0):
                    print("\n")
                else:
                    print('*', end=' ')
            print()
