#!/usr/bin/python3
"""Changes comes from within task"""
from typing import List
def makeChange(coins: List, total):
    """Returns fewest number of coins needed to meet the total"""
    my_coins = sorted(coins, reverse=True)
    if total <= 0:
        return 0
    indx = 0
    lencoins = len(coins)
    for count in my_coins:
        if total > count:
            total = total - my_coins
            indx += 1
            
