#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of boxes, each containing a list of keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  # The first box is unlocked

    keys = [0]  # Start with the keys in the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:  # Ensure the key is valid and the box is not yet unlocked
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)



