#!/usr/bin/python3

def print_last_digit(number):
    if number > 0:
        num = str(number)
        return num[-1]
    elif number < 0:
        num = str(number)
        return -num[-1]
    else:
        return 0
