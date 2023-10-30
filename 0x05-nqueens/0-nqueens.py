#!/usr/bin/python3
"""Gets the number of queens on the board"""

def isvalid(board, row, col):
    for prev in range(row):
        if board[prev] == col or board[prev] - prev == col - row or board[prev] + prev == col + row:
            return False
    return True

def solve_nqueens(n):
    def backtracking(row):
        if row == n:
            sol.append(board[:])
            return
        for col in range(n):
            if isvalid(board, row, col):
                board[row] = col
                backtracking(row + 1)
                board[row] = -1
    board =[-1] * n
    sol = []
    backtracking(0)
    return sol