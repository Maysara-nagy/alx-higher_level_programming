#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
strNumber = str(number)
lDigit = int(strNumber[-1])
if number < 0:
    lDigit = -lDigit
    if lDigit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, lDigit))
    elif lDigit < 6 and lDigit != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, lDigit))
    elif lDigit == 0:
        print("Last digit of {} is {} and is 0".format(number, lDigit))
elif number > 0:
    if lDigit > 5:
        print("Last digit of {} is {} and is greater than 5".format(number, lDigit))
    elif lDigit < 6 and lDigit != 0:
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, lDigit))
    elif lDigit == 0:
        print("Last digit of {} is {} and is 0".format(number, lDigit))
else:
    print("Last digit of {} is {} and is 0".format(number, lDigit))

