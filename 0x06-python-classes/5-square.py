#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Represent the square class."""

    def __init__(slef, size=0):
        """Initialize a new Square."""
        slef.__size = size

    @property
    def size(self):
        """getters"""
        return self.__size

    @size.setter
    def size(self, value):
        """setters"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return the size of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print # to draw the square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
