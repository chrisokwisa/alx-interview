#!/usr/bin/python3
"""Solve the N queens using the backtracking solutions """
import sys


def nqueens(n, board, row, result):
    """takes the four arguments n, the number of the queens
    board, the current state of the chessboard row...   """
    if row == n:
        result.append(list(board))
        return
    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            nqueens(n, board, row + 1, result)


def is_valid(board, row, col, n):
    """ checks if the current placement of a queen is valid
    i,e not attacking any other queens"""
    for i in range(row):
        if board[i] == col or \
                abs(board[i] - col) == abs(i - row):
            return False
    return True


def main():
    """ calls the nqueen function and appends the solution
    to result when all the queens have been placed"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [-1 for i in range(n)]
    result = []
    nqueens(n, board, 0, result)
    for sol in result:
        print(sol)


if __name__ == "__main__":
    main()
