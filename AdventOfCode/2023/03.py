from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    sum = 0
    for r, row in enumerate(rows):
        v = ''
        adjacent = False
        for c, n in enumerate(row):
            if n.isdigit():
                v += n
                if not adjacent:
                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            if r + i >= 0 and r + i < len(rows) and c + j >= 0 and c + j < len(row):
                                ch = rows[r+i][c+j]
                                if ch != '.' and not ch.isdigit():
                                    adjacent = True
            else:
                if adjacent and v:
                    sum += int(v)
                v = ''
                adjacent = False
        if adjacent and v:
            sum += int(v)
    return sum


def part2(data):
    rows = parse_data(data)
    sum = 0

    gear_nums = defaultdict(list)
    for r, row in enumerate(rows):
        v = ''
        gear_points = set()
        for c, n in enumerate(row):
            if n.isdigit():
                v += n
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if r + i >= 0 and r + i < len(rows) and c + j >= 0 and c + j < len(row):
                            ch = rows[r+i][c+j]
                            if ch == '*':
                                gear_points.add((r+i,c+j))
            else:
                for gp in gear_points:
                    gear_nums[gp].append(int(v))
                v = ''
                gear_points = set()
        for gp in gear_points:
            gear_nums[gp].append(int(v))
    for vs in gear_nums.values():
        if len(vs) == 2:
            sum += vs[0] * vs[1]
    return sum


def parse_data(data):
    rows = data.split('\n')
    return rows
