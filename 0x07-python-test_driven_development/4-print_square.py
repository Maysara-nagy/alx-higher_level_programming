#!/usr/bin/python3
"""Write a function that prints a square with the character #."""


def print_square(size):
    """print_square function"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size < 0 and not isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
    