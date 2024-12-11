from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, to_int_array, in_bounds, P, O_DIRS
import sys

debug = False


def part1(data):
    rows = parse_data(data)
    m = to_int_array(rows)

    score = 0
    tops_m = defaultdict(set)
    for y, r in enumerate(m):
        for x, h in enumerate(r):
            if h == 0:
                score += len(find_tops(P(x, y), m, tops_m))
    return score


def find_tops(p, m, tops_m):
    if p in tops_m:
        return tops_m[p]

    tops = set()
    h = m[p.y][p.x]
    if h == 9:
        return {p}

    for dx, dy in O_DIRS:
        np = p + P(dx, dy)
        if in_bounds(np, m) and m[np.y][np.x] == h + 1:
            tops = tops.union(find_tops(np, m, tops_m))
    tops_m[p] = tops
    return tops


def part2(data):
    rows = parse_data(data)
    m = to_int_array(rows)

    score = 0
    tops_m = defaultdict(int)
    for y, r in enumerate(m):
        for x, h in enumerate(r):
            if h == 0:
                score += find_tops2(P(x, y), m, tops_m)
    return score


def find_tops2(p, m, tops_m):
    if p in tops_m:
        return tops_m[p]

    tops = 0
    h = m[p.y][p.x]
    if h == 9:
        return 1

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        np = p + P(dx, dy)
        if in_bounds(np, m) and m[np.y][np.x] == h + 1:
            tops += find_tops2(np, m, tops_m)
    tops_m[p] = tops
    return tops


def parse_data(data):
    rows = data.split('\n')
    return rows
