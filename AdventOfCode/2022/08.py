from collections import defaultdict, deque, namedtuple
import functools
import math
import re


Direction = namedtuple("Direction", 'dir x y')
UP = Direction('up', 0, -1)
LEFT = Direction('left', -1, 0)
DOWN = Direction('down', 0, 1)
RIGHT = Direction('right', 1, 0)


class Tree(object):
    def __init__(self, value):
        self.value = int(value)
        self.dirs = {}
        self.seeing_distances = {}


def in_bounds(grid, y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])


def get_max_height(grid, y, x, dir):
    y = y + dir.y
    x = x + dir.x
    if in_bounds(grid, y, x):
        t = grid[y][x]
        return max(t.dirs[dir.dir], t.value)
    else:
        return -1


def part1(data):
    rows = parse_data(data)

    grid = []
    for row in rows:
        grid.append([Tree(r) for r in row])

    for y, row in enumerate(grid):
        for x, t in enumerate(row):
            t.dirs[UP.dir] = get_max_height(grid, y, x, UP)
            t.dirs[LEFT.dir] = get_max_height(grid, y, x, LEFT)

    for y in range(len(grid) - 1, -1, -1):
        row = grid[y]
        for x in range(len(row) - 1, -1, -1):
            t = row[x]
            t.dirs[DOWN.dir] = get_max_height(grid, y, x, DOWN)
            t.dirs[RIGHT.dir] = get_max_height(grid, y, x, RIGHT)

    visible = 0
    for y, row in enumerate(grid):
        for x, t in enumerate(row):
            if any([t.value > v for v in t.dirs.values()]):
                visible += 1
    return visible


def get_seeing_distance_horiz(grid, dir):
    if dir == 'left':
        start_x = len(grid[0]) - 1
        end_x = -1
        step_x = -1
    else:
        start_x = 0
        end_x = len(grid[0])
        step_x = 1

    for row in grid:
        pending_trees = []
        for x in range(start_x, end_x, step_x):
            t = row[x]

            while pending_trees:
                pt, pos = pending_trees[-1]
                if t.value < pt.value:
                    break
                pt.seeing_distances[dir] = abs(pos - x)
                pending_trees.pop()

            pending_trees.append((t, x))

        while pending_trees:
            pt, pos = pending_trees.pop()
            pt.seeing_distances[dir] = abs(pos - end_x) - 1


def get_seeing_distance_vert(grid, dir):
    if dir == 'up':
        start_y = len(grid) - 1
        end_y = -1
        step_y = -1
    else:
        start_y = 0
        end_y = len(grid)
        step_y = 1

    for x in range(len(grid[0])):
        pending_trees = []
        for y in range(start_y, end_y, step_y):
            t = grid[y][x]

            while pending_trees:
                pt, pos = pending_trees[-1]
                if t.value < pt.value:
                    break
                pt.seeing_distances[dir] = abs(pos - y)
                pending_trees.pop()

            pending_trees.append((t, y))

        while pending_trees:
            pt, pos = pending_trees.pop()
            pt.seeing_distances[dir] = abs(pos - end_y) - 1


def part2(data):
    rows = parse_data(data)

    grid = []
    for row in rows:
        grid.append([Tree(r) for r in row])

    get_seeing_distance_horiz(grid, LEFT.dir)
    get_seeing_distance_horiz(grid, RIGHT.dir)
    get_seeing_distance_vert(grid, UP.dir)
    get_seeing_distance_vert(grid, DOWN.dir)

    max_scenic_score = 0
    for row in grid:
        for t in row:
            score = math.prod(t.seeing_distances.values())
            max_scenic_score = max(max_scenic_score, score)
    return max_scenic_score


def parse_data(data):
    rows = data.split('\n')
    return rows
