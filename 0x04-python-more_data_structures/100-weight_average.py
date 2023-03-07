#!/usr/bin/env python3

def weight_average(my_list=[]):
    if my_list is not None:
        sum = 0
        num = 0
        for r, c in my_list:
            sum += r*c
            num += c
        return (sum / num)
    else:
        return 0
