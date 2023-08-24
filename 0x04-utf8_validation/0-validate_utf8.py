#!/usr/bin/python3
"""UTF8 validation task"""
from typing import List
def validUTF8(data: List[int]) -> bool:
    """UTF8 Validation"""
    counter = 0
    for count in data:
        if counter == 0:
            if count >> 4 == 0b1110:
                counter = 2
            elif count >> 3 == 0b11110:
                counter = 3
            elif count >> 5 == 0b110:
                counter = 2
            elif count >> 7 == 0b1 or count >> 7 != 0:
                return False
        else:
            if count >> 6 != 0b10:
                return False
            counter -= 1
    return counter == 0