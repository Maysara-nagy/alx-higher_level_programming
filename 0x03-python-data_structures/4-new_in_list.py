#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    elif my_list is None:
        return
    else:
        newlist = list(my_list)
        newlist[idx] = element
        return newlist
