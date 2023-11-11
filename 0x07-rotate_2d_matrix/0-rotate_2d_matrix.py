#!/usr/bin/python3
"""Rotating a 2D matrix at 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for count in range(len(matrix)):
        matrix[count].reverse()
    return matrix
