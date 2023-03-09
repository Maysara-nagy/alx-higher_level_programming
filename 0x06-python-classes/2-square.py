#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Represent of Square class"""

    def __init__(self, size=0):
        """initialize a new Square

            Args:
                size (int): size of new square
            Eceptions:
                size must be interger or >= 0
        """
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
        
