#!/usr/bin/python3
"""Write a function that divides all elemets fo a mtrix"""


def matrix_divided(matrix, div):
    """my function to divided a matrix"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if not (len(row) == len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        new_list.append(list(map(lambda x: round(x / div, 2), row)))
    return new_list
    # return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
