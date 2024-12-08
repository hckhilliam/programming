from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, in_bounds
import sys

debug = False

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def part1(data):
    rows = parse_data(data)
    m = to_array(rows)

    pos = get_start_pos(m)
    mapped = set([pos])
    dir_i = 0
    curr_d = dirs[dir_i]

    while True:
        new_pos = (pos[0] + curr_d[0], pos[1] + curr_d[1])
        if not in_bounds(new_pos, m):
            return len(mapped)
        if m[new_pos[1]][new_pos[0]] != '#':
            pos = new_pos
            mapped.add(pos)
        else:
            dir_i = (dir_i + 1) % len(dirs)
            curr_d = dirs[dir_i]


def part2(data):
    rows = parse_data(data)
    m = to_array(rows)

    start_pos = get_start_pos(m)
    pos = start_pos
    mapped = set([pos])
    dir_i = 0
    curr_d = dirs[dir_i]

    while True:
        new_pos = (pos[0] + curr_d[0], pos[1] + curr_d[1])
        if not in_bounds(new_pos, m):
            break
        if m[new_pos[1]][new_pos[0]] != '#':
            pos = new_pos
            mapped.add(pos)
        else:
            dir_i = (dir_i + 1) % len(dirs)
            curr_d = dirs[dir_i]

    cycles = 0
    for p in mapped:
        if p != start_pos:
            x, y = p
            m[y][x] = '#'
            if is_cycle(m, start_pos):
                cycles += 1
            m[y][x] = '.'
    return cycles


def is_cycle(m, start_pos):
    pos = start_pos
    dir_i = 0
    curr_d = dirs[dir_i]
    tracked = set()
    while True:
        new_pos = (pos[0] + curr_d[0], pos[1] + curr_d[1])
        if not in_bounds(new_pos, m):
            return False
        if m[new_pos[1]][new_pos[0]] != '#':
            pos = new_pos
            if (pos, curr_d) in tracked:
                return True
            tracked.add((pos, curr_d))
        else:
            dir_i = (dir_i + 1) % len(dirs)
            curr_d = dirs[dir_i]


def get_start_pos(m):
    for y, r in enumerate(m):
        for x, c in enumerate(r):
            if c == '^':
                return (x, y)


def parse_data(data):
    rows = data.split('\n')
    return rows
