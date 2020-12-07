from collections import defaultdict
import functools
import math

def part1(data):
    rows = parse_data(data)
    first = rows[0].split(',')
    second = rows[1].split(',')
    paths = {}

    f_paths = get_paths(first)
    s_paths = get_paths(second)
    intersections = set(f_paths.keys()).intersection(set(s_paths.keys()))

    mi = min(intersections, key=lambda p: abs(p[0]) + abs(p[1]))
    return abs(mi[0]) + abs(mi[1])


def part2(data):
    rows = parse_data(data)
    first = rows[0].split(',')
    second = rows[1].split(',')
    paths = {}

    f_paths = get_paths(first)
    s_paths = get_paths(second)
    intersections = set(f_paths.keys()).intersection(set(s_paths.keys()))

    mi = min(intersections, key=lambda p: f_paths[p] + s_paths[p])
    return f_paths[mi] + s_paths[mi]


def get_paths(directions):
    x = 0
    y = 0
    paths = {}
    steps = 0
    for f in directions:
        d = f[0]
        n = int(f[1:])
        dx = 0
        dy = 0
        if d == 'R':
            dx = 1
        elif d == 'L':
            dx = -1
        elif d == 'U':
            dy = -1
        else:
            dy = 1
        for i in range(n):
            steps += 1
            x += dx
            y += dy
            if (x, y) not in paths:
                paths[(x, y)] = steps
    return paths


def parse_data(data):
    rows = data.split('\n')
    return rows
