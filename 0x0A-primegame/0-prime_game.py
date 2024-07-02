#!/usr/bin/python3
"""
Prime game module
"""


def prime(n):
    """gives a number of the prime numbers"""
    primes = list(range(2, n+1))
    for _num in primes:
        for num in range(_num + 1, n + 1):
            if not num % _num:
                try:
                    primes.remove(num)
                except ValueError:
                    pass
    return len(primes)


def isWinner(x, nums):
    """determines winner

    :param x: number of rounds
    :type x: int
    :param nums: list of numbers
    :type nums: list[int]
    :return: name of winner
    :rtype: str | None
    """
    pl = {'Ben': 0, 'Maria': 0}
    if x > len(nums):
        return None
    i = 0
    while i < x:
        if nums[i] < 2:
            pl['Ben'] += 1
            i += 1
            continue
        num = prime(nums[i])
        if num % 2:
            pl['Maria'] += 1
        else:
            pl['Ben'] += 1
        i += 1
    if pl['Maria'] == pl['Ben']:
        return None
    res = 'Ben' if pl['Ben'] > pl['Maria'] else 'Maria'
    return res
