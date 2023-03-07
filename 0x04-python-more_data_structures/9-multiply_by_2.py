#!/usr/bin/python3
# Write a function that returns a new
# dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for keys in a_dictionary.keys():
        new_dic[keys] *= 2
    return new_dic
