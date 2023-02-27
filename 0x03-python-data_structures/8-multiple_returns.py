#!/usr/bin/python3


def multiple_returns(sentence):
    my_tuple = tuple(sentence)
    #first = my_tuple[0]
    len1 = len(my_tuple)
    if sentence is None:
        first = 0
    else:
        first = my_tuple[0]
    return (len1, first)
