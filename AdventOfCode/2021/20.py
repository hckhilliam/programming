from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows, mapper = parse_data(data)
    for i in range(2):
        rows = enhance(rows, mapper, is_dark=i % 2 == 0)

    lights = 0
    for r in rows:
        for c in r:
            if c == '#':
                lights += 1
    return lights


def enhance(rows, mapper, is_dark):
    new_rows = []
    # Enhanced map has 2 extra spots
    for i in range(-1, len(rows) + 1):
        new_row = []
        for j in range(-1, len(rows[0]) + 1):
            b = ''
            for i2 in range(i - 1, i + 2):
                for j2 in range(j - 1, j + 2):
                    if in_bounds(i2, j2, rows):
                        b += '1' if rows[i2][j2] == '#' else '0'
                    else:
                        b += '0' if is_dark else '1'
            index = int(b, 2)
            new_row.append(mapper[index])
        new_rows.append(new_row)
    return new_rows


def in_bounds(i, j, rows):
    return i >= 0 and i < len(rows) and j >= 0 and j < len(rows[0])


def part2(data):
    rows, mapper = parse_data(data)
    for i in range(50):
        rows = enhance(rows, mapper, is_dark=i % 2 == 0)

    lights = 0
    for r in rows:
        for c in r:
            if c == '#':
                lights += 1
    return lights


def parse_data(data):
    rows = data.split('\n')
    mapper = rows[0]
    rows = rows[2:]
    return rows, mapper
