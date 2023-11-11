#!/usr/bin/python3
"""Gets the number of queens on the board"""

import sys


def validate_input(args):
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not args[1].isdigit():
        print("N must be a number")
        exit(1)
    layout = int(args[1])
    if layout < 4:
        print("N must be at least 4")
        exit(1)
    return layout


def is_safe(board, row, col):
    for prev_row, prev_col in board:
        if col == prev_col or \
           col == prev_col - (row - prev_row) or \
           col == prev_col + (row - prev_row):
            return False
    return True


def solve_nqueens(layout):
    def solve(row, board, result):
        if row == layout:
            result.append(board[:])
            return
        for col in range(layout):
            if is_safe(board, row, col):
                board.append((row, col))
                solve(row + 1, board, result)
                board.pop()

    result = []
    solve(0, [], result)
    return result

if __name__ == "__main__":
    layout = validate_input(sys.argv)
    solutions = solve_nqueens(layout)
    for solution in solutions:
        print(solution)


# def is_safe(board, row, col, number):
#     """Checks if the board is safe"""
#     for i in range(col):
#         if board[i] == row or \
#            board[i] - i == row - col or \
#            board[i] + i == row + col:
#             return False
#     return True

# def print_board(board):
#     """Prints out the board"""
#     print([[i, board[i]] for i in range(len(board))])

# def solve_nqueens_util(board, col, number):
#     """Solves for the queen"""
#     if col == number:
#         print_board(board)
#         return True

#     res = False
#     for i in range(number):
#         if is_safe(board, i, col, number):
#             board[col] = i
#             res = solve_nqueens_util(board, col + 1, number) or res
#             board[col] = -1

#     return res

# def solve_nqueens(number):
#     """Solves for the queen"""
#     board = [-1] * number

#     if not solve_nqueens_util(board, 0, number):
#         return False

#     return True

# def validate(args):
#     """Validates the arguments"""
#     if len(args) == 2:
#         try:
#             number = int(args[1])
#             if number < 4:
#                 raise ValueError("N must be at least 4")
#             return number
#         except ValueError:
#             print("N must be a number")
#             exit(1)
#     else:
#         print("Usage: nqueens N")
#         exit(1)

# if __name__ == "__main__":
#     """Execution"""
#     number = validate(sys.argv)
#     solve_nqueens(number)
