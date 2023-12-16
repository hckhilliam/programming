from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    progress = [list(r) for r in rows]
    lit = defaultdict(set)
    traverse(rows, start=(0, 0), d=(1, 0), lit=lit, progress=progress)

    return len(lit.keys())


def traverse(rows, start, d, lit, progress):
    x, y = start
    dx, dy = d

    while y >= 0 and y < len(rows) and x >= 0 and x < len(rows[y]):
        if (dx, dy) in lit[(x, y)]:
            return
        lit[(x, y)].add((dx, dy))

        progress[y][x] = '#'
        # for r in progress:
        #     print(''.join(r))
        # print()

        c = rows[y][x]
        if c == '/':
            tempX = dx
            dx = -dy
            dy = -tempX
        elif c == '\\':
            dx, dy = dy, dx
        elif c == '|' and dx != 0:
            traverse(rows, start=(x, y), d=(0, 1), lit=lit, progress=progress)
            traverse(rows, start=(x, y), d=(0, -1), lit=lit, progress=progress)
            return
        elif c == '-' and dy != 0:
            traverse(rows, start=(x, y), d=(1, 0), lit=lit, progress=progress)
            traverse(rows, start=(x, y), d=(-1, 0), lit=lit, progress=progress)
            return

        x += dx
        y += dy


def part2(data):
    rows = parse_data(data)
    progress = [list(r) for r in rows]

    max_energized = 0
    for y in range(len(rows)):
        lit = defaultdict(set)
        traverse(rows, start=(0, y), d=(1, 0), lit=lit, progress=progress)
        max_energized = max(max_energized, len(lit.keys()))
        lit = defaultdict(set)
        traverse(rows, start=(len(rows[y]) - 1, y), d=(-1, 0), lit=lit, progress=progress)
        max_energized = max(max_energized, len(lit.keys()))
    for x in range(len(rows[0])):
        lit = defaultdict(set)
        traverse(rows, start=(x, 0), d=(0, 1), lit=lit, progress=progress)
        max_energized = max(max_energized, len(lit.keys()))
        lit = defaultdict(set)
        traverse(rows, start=(x, len(rows) - 1), d=(0, -1), lit=lit, progress=progress)
        max_energized = max(max_energized, len(lit.keys()))

    return max_energized


def parse_data(data):
    rows = data.split('\n')
    return rows
