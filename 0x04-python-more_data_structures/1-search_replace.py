#!/usr/bin/python3
#Write a function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    tmp = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            tmp.append(replace)
        else:
            tmp.append(my_list[i])
    return tmp
