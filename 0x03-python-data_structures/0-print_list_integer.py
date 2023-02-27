#!/usr/bin/python3
#0. Print a list of integers

def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{}".format(int(my_list[i])))
