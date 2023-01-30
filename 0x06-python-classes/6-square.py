#!/usr/bin/python3

class Square:
    """
    Class describing a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """

        Args:
            size (int, optional): Size of the square's sides. Defaults to 0.
            position (tuple, optional): 2 positive integers
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """Retrieves the value of position

        Returns:
            tuple: Tuple of 2 integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of position as 2 integers after checking type & count

        Args:
            value (tuple): Two integers

        Raises:
            TypeError: Raises error when value provided is not 2 integers
        """
        value: tuple
        error_str = "position must be a tuple of 2 positive integers"
        if len(value) > 2 and not isinstance(value, tuple):
            raise TypeError(error_str)
        elif isinstance(value, tuple):
            for n in value:
                if isinstance(n, int) and n > 0:
                    pass
                else:
                    raise TypeError(error_str)
            self.__position = value

    @property
    def size(self):
        """Retrieves the value of size

        Returns:
            int: Value of 'size' variable
        """
        return self.__size

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


my_square_2 = Square(6, (3, 5))
my_square_2.position = (2, (4, -4))
print(my_square_2.position)
