#!/usr/bin/python3
"""Prime game Algorithm"""

def isWinner(x, nums):
    """Determines the winner"""
    gamers = {'Maria': 0, 'Ben': 0}

    for count in range(x):
        values = [num for num in range(1, nums[count] + 1)]
        current_turn = 'Maria'
        while values:
            pick = values.pop(0)
            values = [num for num in values if num % pick != 0]
            current_turn = 'Ben' if current_turn == 'Maria' else 'Maria'
        gamers[current_turn] += 1
    if gamers['Maria'] > gamers['Ben']:
        return 'Maria'
    elif gamers['Ben'] > gamers['Maria']:
        return 'Ben'
    else:
        return None