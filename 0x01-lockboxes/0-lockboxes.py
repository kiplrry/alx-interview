#!/usr/bin/python3
"""lockboxes module

"""


def canUnlockAll(boxes: list[list]) -> bool:
    """CanUnlock

    :param boxes: list of boxes with keys
    :type boxes: list[list]
    :return: bool
    :rtype: bool
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
