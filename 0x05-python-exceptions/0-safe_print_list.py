#!/usr/bin/python3
# Write a function that prints x elements of a list.

def safe_print_list(my_list=[], x=0):
    sum = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            sum += 1
        print()
        return sum
    except:
        return sum
