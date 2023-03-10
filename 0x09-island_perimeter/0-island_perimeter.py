#!/usr/bin/python3
""" Should be an executable file """


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for col in range(cols):
        for row in range(rows):
            if grid[row][col] == 1:
                perimeter += 4

                if row != 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                if col != 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                if row + 1 != rows and grid[row + 1][col] == 1:
                    perimeter -= 1
                if col + 1 != cols and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
