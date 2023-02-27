#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is None:
        return (0, 0)
    else:
        my_tuple = tuple(sentence)
        len1 = len(my_tuple)
        first = my_tuple[0]
        return (len1, first)
