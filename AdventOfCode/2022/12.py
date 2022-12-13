from collections import defaultdict, deque
import functools
import math
import re
import sys


def in_bounds(grid, i, j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i])


def find_fewest(grid, start, dest):
    q = deque([(start[0], start[1], 0)])
    visited = {start}
    while q:
        i, j, s = q.popleft()
        if (i, j) == dest:
            return s

        for c in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_i = i + c[0]
            new_j = j + c[1]
            if not in_bounds(grid, new_i, new_j):
                continue
            if (new_i, new_j) in visited:
                continue
            if ord(grid[new_i][new_j]) > ord(grid[i][j]) + 1:
                continue
            visited.add((new_i, new_j))
            q.append((new_i, new_j, s + 1))
    return None


def part1(data):
    rows = parse_data(data)
    grid = []
    start = None
    dest = None
    for i, r in enumerate(rows):
        row = []
        for j, c in enumerate(r):
            if c == 'S':
                row.append('a')
                start = (i, j)
            elif c == 'E':
                row.append('z')
                dest = (i, j)
            else:
                row.append(c)
        grid.append(row)

    return find_fewest(grid, start, dest)


def part2(data):
    rows = parse_data(data)
    grid = []
    starts = []
    dest = None
    for i, r in enumerate(rows):
        row = []
        for j, c in enumerate(r):
            if c == 'S':
                row.append('a')
            elif c == 'E':
                row.append('z')
                dest = (i, j)
            else:
                row.append(c)
            if row[-1] == 'a':
                starts.append((i, j))
        grid.append(row)

    fewest = math.inf
    for s in starts:
        m = find_fewest(grid, s, dest)
        if m:
            fewest = min(m, fewest)
    return fewest


def parse_data(data):
    rows = data.split('\n')
    return rows
