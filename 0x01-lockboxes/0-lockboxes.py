#!/usr/bin/python3
"""
    Determines if all boxes can be opened.

    Args:
        boxes (list of list of int):
        A list of lists where each sublist represents
        the keys contained in a box. The first box (boxes[0])
        is initially unlocked.

    Returns:
        bool: True if all boxes can be opened, otherwise False
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    """

    n = len(boxes)
    opened_boxes = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key not in opened_boxes and key < n:
            opened_boxes.add(key)
            keys.extend(boxes[key])

    return len(opened_boxes) == n
