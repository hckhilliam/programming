from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    risk_level = 0
    for i, r in enumerate(rows):
        for j, n in enumerate(r):
            low = True
            for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if in_bounds(i2, j2, rows) and n >= rows[i2][j2]:
                    low = False
                    break
            if low:
                risk_level += n + 1
    return risk_level


def part2(data):
    rows = parse_data(data)
    low_points = []
    for i, r in enumerate(rows):
        for j, n in enumerate(r):
            low = True
            for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if in_bounds(i2, j2, rows) and n >= rows[i2][j2]:
                    low = False
                    break
            if low:
                low_points.append((i, j))

    basins = []
    for i, j in low_points:
        basins.append(find_basin_size(i, j, rows))
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


def find_basin_size(i, j, rows):
    q = deque([(i, j)])
    v = {(i, j)}
    size = 1
    while q:
        i, j = q.popleft()
        for i2, j2 in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if in_bounds(i2, j2, rows) and (i2, j2) not in v and rows[i2][j2] != 9:
                size += 1
                q.append((i2, j2))
                v.add((i2, j2))
    return size


def in_bounds(i, j, rows):
    return i >= 0 and i < len(rows) and j >= 0 and j < len(rows[0])


def parse_data(data):
    rows = data.split('\n')
    n_rows = []
    for r in rows:
        n_rows.append([int(n) for n in r])
    return n_rows
