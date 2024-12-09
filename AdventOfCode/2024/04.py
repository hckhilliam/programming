from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, in_bounds
import sys

debug = False


def part1(data):
    rows = parse_data(data)

    total = 0
    for y, r in enumerate(rows):
        for x, l in enumerate(r):
            total += count_xmas(l, (x, y), rows)
    return total


def count_xmas(l, p, rows):
    if l != 'X':
        return 0

    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue

            if is_xmas(p, rows, (i, j)):
                count += 1
    return count


def is_xmas(p, rows, d):
    letters = ['M', 'A', 'S']
    for i in range(3):
        p = (p[0] + d[0], p[1] + d[1])
        if not in_bounds(p, rows) or rows[p[1]][p[0]] != letters[i]:
            return False
    return True


def part2(data):
    rows = parse_data(data)

    total = 0
    for y, r in enumerate(rows):
        for x, l in enumerate(r):
            if is_x_mas(l, (x, y), rows):
                total += 1
    return total


def is_x_mas(l, p, rows):
    if l != 'A':
        return False

    letters = {'M', 'S'}
    d1 = {get_letter(p, rows, (-1, -1)), get_letter(p, rows, (1, 1))}
    d2 = {get_letter(p, rows, (-1, 1)), get_letter(p, rows, (1, -1))}
    if letters == d1 == d2:
        return True
    return False


def get_letter(p, rows, d):
    p = (p[0] + d[0], p[1] + d[1])
    if not in_bounds(p, rows):
        return None
    return rows[p[1]][p[0]]


def parse_data(data):
    rows = data.split('\n')
    return rows
