#!/usr/bin/python3

def print_last_digit(number):
    if number > 0:
        num = str(number)
        print(num[-1], end='')
        return num[-1]
    elif number < 0:
        num = str(number)
        print(-int(num[-1]), end='')
        return -int(num[-1])
    else:
        print("0", end='')
        return 0
