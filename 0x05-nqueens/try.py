#!/usr/bin/python3
from sys import argv
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

size = int(argv[1])
queens = [[0,0], [1, 2]]
rem = []

def do(start, size):
    for i in range(size):
        for j in range(size):
            point = [i, j]
            if point in queens:
                print(f'{bcolors.OKGREEN}({i}, {j}){bcolors.ENDC}', end='')
                continue
            if check(point):
                queens.append([i, j])
                print(f'{bcolors.OKGREEN}({i}, {j}){bcolors.ENDC}', end='')
            else:
                print(f'{bcolors.FAIL}({i}, {j}){bcolors.ENDC}', end='')
        print()
    if len(queens) != size:
        do()






def check(point: list[int, int])-> bool:
    """checks if a point is valid"""
    for queen in queens:
        if point[0] == queen[0] or\
            point[1] == queen[1]:
            return False
        diff = [abs(point[0] - queen[0]), abs(point[1] - queen[1])]
        if diff[0] == diff[1]:
            return False
    return True

do(size)