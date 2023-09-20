#!/usr/bin/python3
'''A function that determines if all boxes can be opened'''
from typing import List
def canUnlockAll(boxes: List[list]) -> bool:
    """A method which determines if all boxes can be opened"""
    # total = len(boxes)
    # if not total:
    #     return False
    # first_keys = [0]
    # for i in first_keys:
    #     for j in boxes[i]:
    #         if j != first_keys and j < total:
    #             first_keys.append(j)
    # return len(first_keys) == total
    first_box = [0]

    for count in first_box:
        for idx in boxes[count]:
            if idx not in first_box and idx < len(boxes):
                first_box.append(idx)
                if len(first_box) == len(boxes):
                    return True
    return False