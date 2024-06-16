#!/usr/bin/python3
"""
   method that determines if all the boxes can be opened
   if an n number of locked boxes, Each box numbered sequentially
   0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
        Parameter: boxes
        Return: True or False
    """
    if not boxes[0] and len(boxes) > 1:
        return False

    oldkeys = set()
    allBoxes = [i for i in range(len(boxes))]
    allBoxes.remove(0)

    oldkeys.update(boxes[0])
    newkeys = oldkeys.copy()
    while True:
        for key in (set(allBoxes) & oldkeys):
            if key != 0:
                allBoxes.remove(key)
                newkeys.update(boxes[key])
        if len(allBoxes) == 0:
            return True
        if oldkeys == newkeys:
            return False
        oldkeys = newkeys.copy()
