#!/usr/bin/env python3
#Write a function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda i : i**2, i)))
    return new_matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)