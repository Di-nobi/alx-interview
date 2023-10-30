#!/usr/bin/python3
"""Minimum Operations Interview question"""
import math

def factors(n):
    """Gets the factors"""
    myList = list()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            myList.append(i)
            n //= i
    if n > 2:
        myList.append(n)
    return myList
def minOperations(n):
    """A method that calculates the fewest number of 
    operations needed to result in n H"""
    if not isinstance(n, int) or n < 2:
        return 0
    return sum(factors(n))