#!/usr/bin/env python

"""
An example collaborative project 
"""


def is_50_in_list(low, high):
    """
    Loops over all values checking if it is 50
    """
    for i in range(low, high):
        if i == 50:
            return True
    return False



if __name__ == "__main__":

    # test the code on a range
    print(is_50_in_list(1, 10))
    print(is_50_in_list(50, 100))
    print(is_50_in_list(30, 80))
