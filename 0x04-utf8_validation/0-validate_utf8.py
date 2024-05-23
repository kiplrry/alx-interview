#!/usr/bin/python3
"""UTF-8 validation module"""

byt = {
    '1': 0b0,
    '2': 0b110,
    '3': 0b1110,
    '4': 0b11110
    }


def validUTF8(data: list) -> bool:
    """validation function"""
    if not data:
        return False
    for char in data:
        if char.bit_length() != 8:
            return False
    new_lst = data
    while new_lst:
        res, byt_num = checker(new_lst[0])
        if not res:
            return False
        print(int(byt_num))
        if int(byt_num) > 1:
            print(2322233)
            whole_list = new_lst[:int(byt_num)]
            res2 = one_zero_checker(whole_list, int(byt_num))
            if not res2:
                return False
        new_lst = new_lst[int(byt_num):]
    return True


def checker(char: int) -> list[bool, str]:
    '''checks if char is legit'''
    for b, k in byt.items():
        res = k ^ (char >> (8 - k.bit_length()))
        if not res:
            return [True, b]
    return [False, None]


def one_zero_checker(ls: list, num: int):
    '''checks if list is valid'''
    if num > len(ls) + 1:
        return False
    for char in ls:
        res = 0b10 ^ (char >> 6)
        if res:
            return False
    return True
