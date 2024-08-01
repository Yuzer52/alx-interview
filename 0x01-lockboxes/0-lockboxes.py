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
    if not isinstance(boxes, list):
        return False
    # Check if the list is empty
    if len(boxes) == 0:
        return False

    for k in range(1, len(boxes)):
        boxes_checked = False
        # Check each box to see if it contains the key for box k
        for idx, box in enumerate(boxes):
            if k in box and k != idx:
                boxes_checked = True
                break
        if not boxes_checked:
            return False
    return True

