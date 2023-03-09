#!/usr/bin/python3

"""Define Square class."""


class Square:
    """Represent a class Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getters"""
        return self.__size

    @size.setter
    def size(self, value):
        """setters"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """setters for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """getters"""
        if (not isinstance(value, tuple) and len(value) != 2) and not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """print the square by #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
