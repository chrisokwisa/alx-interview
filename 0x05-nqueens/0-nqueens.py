#!/usr/bin/python3
"""Solve the N queens using the backtracking solutions """
import sys


def nqueens(n):
    """# function to solve N queens problem
    # implementation of backtracking algorithm
    """
    def is_not_under_attack(row, col):
        # check if a queen can be placed in cell (row, col)
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                board[row] = col
                solve(row + 1)

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    result = []
    solve(0)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    result = nqueens(n)
    for sol in result:
        print(sol)
