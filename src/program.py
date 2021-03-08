#!/usr/bin/env python

"""
An example collaborative project 
"""


def is_50_in_list(low, high):
    """
    Finds whether 50 is within a range of values.
    """
    return 50 in range(low, high)


if __name__ == "__main__":

    # test the code on a range
    print(is_50_in_list(1, 10))
    print(is_50_in_list(50, 100))
    print(is_50_in_list(30, 80))
