#!/usr/bin/python3
"""
function for determining if all
boxes in a given list can be opened.
"""


def canUnlockAll(boxes):
    """
    This function takes a list of lists and returns a boolean indicating
        whether all boxes in the list can be opened. A key with the same
        number as a box opens that box. You can assume all keys will be
        positive integers. There can be keys that do not have boxes.
        The first box boxes[0] is unlocked.
   """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)
