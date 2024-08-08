#!/usr/bin/python3
""" Minimum Operations
    This module defines a function to calculate the minimum
    number of operations needed to achieve exactly n 'H' characters
    in a text file using only 'Copy All' and 'Paste' operations.
"""

def minOperations(n: int) -> int:
    """ 
    Calculate the minimum operations needed to result in exactly n 'H' characters.
    
    Args:
        n (int): The target number of 'H' characters.
    
    Returns:
        int: The minimum number of operations needed to achieve n 'H' characters,
             or 0 if it is impossible to achieve exactly n 'H' characters.
    """
    
    copied = 'H'
    current = 'H'
    operations = 0
    
    while len(current) < n:
        if n % len(current) == 0:
            operations += 2
            copied = current
            current += current
        else:
            operations += 1
            current += copied
    
    if len(current) != n:
        return 0
    
    return operations

