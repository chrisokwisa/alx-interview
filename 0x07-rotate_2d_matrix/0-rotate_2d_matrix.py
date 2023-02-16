#!/usr/bin/python3
"""Indicates the script should be executed as an executable program"""


def rotate_2d_matrix(matrix):
    """ Rotates it 90 degrees clockwise """
    n = len(matrix)
    # Traverse the matrix in layers
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[first][i]

            # Move left to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom to left
            matrix[last - (i - first)
                   ][first] = matrix[last][last - (i - first)]

            # Move right to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top to right
            matrix[i][last] = top
