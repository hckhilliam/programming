from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    numbers, boards = parse_data(data)

    for bingo_n in numbers:
        for board in boards:
            for r, row in enumerate(board):
                for c, n in enumerate(row):
                    if n == bingo_n:
                        board[r][c] = ''
                        if check_win(r, c, board):
                            return points(bingo_n, board)


def part2(data):
    numbers, boards = parse_data(data)
    wins = set()

    for bingo_n in numbers:
        for i, board in enumerate(boards):
            if i in wins:
                continue
            for r, row in enumerate(board):
                for c, n in enumerate(row):
                    if n == bingo_n:
                        board[r][c] = ''
                        if check_win(r, c, board):
                            wins.add(i)
                            if len(wins) == len(boards):
                                return points(bingo_n, board)


def parse_data(data):
    rows = data.split('\n')

    numbers = rows[0].split(',')
    boards = []
    i = 2
    board = []
    while i < len(rows):
        while i < len(rows) and len(rows[i]):
            board.append(rows[i].split())
            i += 1
        i += 1
        boards.append(board)
        board = []
    return numbers, boards


def check_win(r, c, board):
    column_win = True
    for i in range(len(board)):
        if board[(r + i) % len(board)][c] != '':
            column_win = False
    row_win = True
    for i in range(len(board[0])):
        if board[r][(c + i) % len(board[0])] != '':
            row_win = False
    return row_win or column_win


def points(bingo_n, board):
    board_points = 0
    for r in board:
        for n in r:
            if n != '':
                board_points += int(n)
    return board_points * int(bingo_n)


def pretty_print_board(board):
    for r in board:
        print(r)
