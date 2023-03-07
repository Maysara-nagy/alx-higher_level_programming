#!/usr/bin/python3
# Technical interview preparation:

def roman_to_int(roman_string):
    if roman_string not None or type(roman_string) == str:
        roman = list(roman_string)
        sum = 0
        for i in roman:
            if i == 'I':
                sum += 1
            if i == 'V':
                sum += 5
            if i == 'X':
                sum += 10
            if i == 'L':
                sum += 50
            if i == 'D':
                sum += 500
            if i == 'M':
                sum += 1000
        return sum
    else:
        return 0
