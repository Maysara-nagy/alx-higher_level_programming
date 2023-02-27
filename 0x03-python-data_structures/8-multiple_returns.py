#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        first = 0
    else:
        my_tuple = tuple(sentence)
        first = my_tuple[0]
        len1 = len(my_tuple)
        return (len1, first)
