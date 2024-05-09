#!/usr/bin/python3
"""
In a text file, thereis a single character H.
Your text editor can execute only two operations in
this file: Copy All and Paste. Given a number n,
write a method that calculates the fewest
number of operations needed to result in exactly
n H characters in the file.
"""
from typing import List, Tuple


def minOperations(n: int) -> int:
    """
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 0 or not isinstance(int):
        return 0
    lst = []
    num = n
    while True:
        fact, new = getfact(num)
        lst.append(fact)
        if new == 0:
            break
        num = new
    lst = [num - 1 for num in lst]
    num = sum(lst) + len(lst)
    return num


def getfact(n: int) -> Tuple[int, int]:
    """
    get the factor of the number
    """
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            return i, int(n / i)
    return n, 0
