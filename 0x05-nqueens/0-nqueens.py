#!/usr/bin/python3
'''N-Queens Challenge'''

import sys

def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row, board, result):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(n, row + 1, board, result)

    result = []
    place_queens(n, 0, [-1] * n, result)
    return result

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(int(sys.argv[1]))
    for idx, val in enumerate(solutions):
        if idx == len(solutions) - 1:
            print(val, end='')
        else:
            print(val)
