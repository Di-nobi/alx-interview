#!/usr/bin/python3
"""Prime game winner"""


def isWinner(x, nums):
    """Prime game winner determination"""
    if x < 1 or not nums:
        return None
    m_wins = 0
    b_wins = 0
    n_max = max(nums)
    primes = [True] * (n_max + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n_max**0.5) + 1):
        if primes[p]:
            for multiple in range(p**2, n_max + 1, p):
                primes[multiple] = False

    for n in nums:
        if primes[n]:
            b_wins += 1
        else:
            count = sum(primes[2:n + 1])
            m_wins += count % 2 == 0
            b_wins += count % 2 == 1

    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'
