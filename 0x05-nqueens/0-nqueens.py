#!/usr/bin/python3
"""Gets the number of queens on the board"""

import sys

def is_safe(board, row, col, number):
    """Checks if the board is safe"""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def print_board(board):
    """Prints out the board"""
    print([[i, board[i]] for i in range(len(board))])

def solve_nqueens_util(board, col, number):
    """Solves for the queen"""
    if col == number:
        print_board(board)
        return True

    res = False
    for i in range(number):
        if is_safe(board, i, col, number):
            board[col] = i
            res = solve_nqueens_util(board, col + 1, number) or res
            board[col] = -1

    return res

def solve_nqueens(number):
    """Solves for the queen"""
    board = [-1] * number

    if not solve_nqueens_util(board, 0, number):
        return False

    return True

def validate(args):
    """Validates the arguments"""
    if len(args) == 2:
        try:
            number = int(args[1])
            if number < 4:
                raise ValueError("N must be at least 4")
            return number
        except ValueError:
            print("N must be a number")
            exit(1)
    else:
        print("Usage: nqueens N")
        exit(1)

if __name__ == "__main__":
    """Execution"""
    number = validate(sys.argv)
    solve_nqueens(number)
