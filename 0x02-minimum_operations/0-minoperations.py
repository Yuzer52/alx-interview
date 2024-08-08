#!/usr/bin/python3
""" Script that computes the minimum number of operations
    needed to achieve exactly n 'H' characters using only
    Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to result
    in exactly n 'H' characters using Copy All and Paste operations.

    Args:
        n (int): The target number of 'H' characters.
                factor_list: List to save the operations
    Return:
        int: The minimum number of operations required to achieve
             n 'H' characters, or 0 if n is less than 2.
    """
    if n < 2:
        return 0

    factor_list = []
    i = 1

    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)

    return sum(factor_list)
