#!/usr/bin/python3
"""
Finds the peak value in a list of unsorted integers
Used the inbuilt set and max functions
"""


def find_peak(list_of_integers):
    """
    Puts ints in a set then use max to find peak
    """
    if len(list_of_integers) == 0:
        return None

    int_set = set(list_of_integers)
    return max(int_set)
