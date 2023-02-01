#!/usr/bin/python3
""" Contain a script that gets the nQueens """


import sys


def is_not_attacked(board, row, col, N):
    # check if there is a queen in the same row or col

    for i in range(N):
        if board[row][i] or board[i][col]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve(board, col, N, solutions):
    if col >= N:
        solutions.append([(i, j) for i,
                          row in enumerate(board) for j, val
                          in enumerate(row) if val])
        return

    for i in range(N):
        if is_not_attacked(board, i, col, N):
            board[i][col] = 1
            solve(board, col + 1, N, solutions)
            board[i][col] = 0


def nqueens(N):
    if type(N) != int:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

        n = int(sys.argv[1])
        nqueens(n)
