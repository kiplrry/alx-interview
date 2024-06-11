#!/usr/bin/python3
"""rotating a 2d matrix
"""


def rotate_2d_matrix(matrix: list):
    """Rotate 2d matrix

    :param matrix: 2D matrix
    :type matrix: list
    """

    matrix.reverse()
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if j > i:
                continue
            matrix[i][j], matrix[j][i]\
                = matrix[j][i], matrix[i][j]
