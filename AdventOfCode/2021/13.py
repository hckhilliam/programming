from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    grid, instructions = parse_data(data)
    for direction, n in instructions:
        new_grid = fold(grid, direction, n)
        grid = new_grid
        break
    return len(grid)


def part2(data):
    grid, instructions = parse_data(data)
    for direction, n in instructions:
        new_grid = fold(grid, direction, n)
        grid = new_grid
    print_grid(grid)
    return None


def fold(grid, direction, n):
    new_grid = set()
    end = n * 2
    for x, y in grid:
        if direction == 'y':
            if y < n:
                new_grid.add((x, y))
            elif y <= end:
                new_grid.add((x, end - y))
        else:
            if x < n:
                new_grid.add((x, y))
            elif x <= end:
                new_grid.add((end - x, y))
    return new_grid


def print_grid(grid):
    x = [p[0] for p in grid]
    y = [p[1] for p in grid]
    max_x = max(x)
    max_y = max(y)

    for y in range(max_y + 1):
        row = ''
        for x in range(max_x + 1):
            if (x, y) in grid:
                row += '#'
            else:
                row += '.'
        print(row)


def parse_data(data):
    rows = data.split('\n')
    i = False
    grid = set()
    instructions = []
    for r in rows:
        if not r.strip():
            i = True
        elif not i:
            x, y = r.split(',')
            grid.add((int(x), int(y)))
        else:
            foldline = r.split(' ')[-1]
            direction, n = foldline.split('=')
            instructions.append((direction, int(n)))
    return grid, instructions
