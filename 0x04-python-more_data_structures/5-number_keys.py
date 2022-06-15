#!/usr/bin/python3


def number_keys(a_dictionary):
    """
    A function that returns the number of keys in a dictionary.
    """
    count = 0
    #.items() returns number of keys in a dictionary
    for key in a_dictionary.items():
        count += 1
    return count
