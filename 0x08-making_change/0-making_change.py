#!/usr/bin/python3
"""Changes comes from within task"""
from typing import List


def makeChange(coins: List, total):
    """Returns fewest number of coins needed to meet the total"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for count in range(len(coins)):
        while total >= coins[count]:
            total -= coins[count]
            num_coins += 1
    return num_coins if total == 0 else -1
