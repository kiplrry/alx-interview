#!/usr/bin/python3
"""alx interview question"""


def pascal_triangle(n):
    """The question:
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the Pascal's triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    arr = []
    prev_arr = [1]
    for i in range(1, n+1):
        curr_arr = []
        for j in range(i):
            if (j - 1) < 0:
                prev_elem = 0
            else:
                prev_elem = prev_arr[j - 1]
            if j >= len(prev_arr):
                cur_elem = 0
            else:
                cur_elem = prev_arr[j]
            sum = prev_elem + cur_elem
            curr_arr.append(sum)
        arr.append(curr_arr)
        prev_arr = curr_arr
    return arr
