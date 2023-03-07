#!/usr/bin/python3
# Write a function that returns
# a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary:
        biggest = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value is biggest:
                return key
    else:
        return None
