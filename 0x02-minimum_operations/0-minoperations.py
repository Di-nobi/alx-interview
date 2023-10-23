#!/usr/bin/python3
"""Minimum Operations Interview question"""

def minOperations(n):
    """A method that calculates the fewest number of 
    operations needed to result in n H"""
    count_move = 0
    counter = 2
    while n > 1:
        while n % 2 == 0:
            count_move += counter
            n //= counter
        counter = counter + 1
    return count_move