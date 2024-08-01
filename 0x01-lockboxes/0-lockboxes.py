#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    # Check if the input is a list
    if type(boxes) is not list:
        return False

    # Check if the list of boxes is empty
    elif len(boxes) == 0:
        return False

    # Initialize a list to keep track of unlocked boxes
    unlocked = [False] * len(boxes)
    unlocked[0] = True  # The first box is always unlocked
    keys = [0]  # Start with the keys in the first box

    # Use keys to unlock boxes iteratively
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and not unlocked[key]:  # Check if key is valid and box is not yet unlocked
                unlocked[key] = True
                keys.append(key)  # Add new key to the list of keys to process

    # Check if all boxes are unlocked
    return all(unlocked)

