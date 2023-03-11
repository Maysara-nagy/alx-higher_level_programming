#!/usr/bin/python3
import sys
sys.path.insert(1, 'C:/Users/Maisara/Desktop/alx-higher_level_programming/0x07-python-test_driven_development')
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)