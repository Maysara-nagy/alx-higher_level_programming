#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, "None")
    else:
        my_tuple = tuple(sentence)
        len1 = len(my_tuple)
        first = my_tuple[0]
        return (len1, first)
