#!/usr/bin/python3
"""Prime game Algorithm"""

# def is_prime(num):
#     if not num or num <= 1:
#         return False
#     for count in range(2, int(num**0.5) + 1):
#         if num % count == 0:
#             return False
#     return True
    
# def isWinner(x, nums):
#     """An algorithm to get the winner"""
#     maria = 0
#     ben = 0

#     for i in nums:
#         slots_avaliable = set(range(2, i + 1))

#         while slots_avaliable:
#             found_prime = False
#             for num in sorted(slots_avaliable):
#                 if is_prime(num):
#                     found_prime = True
#                     slots_avaliable -= set(range(num, i + 1, num))
#                     break
#             if not found_prime:
#                 maria += 1
#                 break
#         else:
#             ben += 1
#     if maria > ben:
#         return "Maria"
#     elif ben > maria:
#         return "Ben"
#     else:
#         return None

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
    return 'Maria' if gamers['Maria'] > gamers['Ben'] else 'Ben'