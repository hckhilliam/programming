from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, to_int_array, in_bounds
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
                score += len(find_tops((x, y), m, tops_m))
    return score


def find_tops(p, m, tops_m):
    if p in tops_m:
        return tops_m[p]

    tops = set()
    h = m[p[1]][p[0]]
    if h == 9:
        return {p}

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        np = (p[0] + dx, p[1] + dy)
        if in_bounds(np, m) and m[np[1]][np[0]] == h + 1:
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
                score += find_tops2((x, y), m, tops_m)
    return score


def find_tops2(p, m, tops_m):
    if p in tops_m:
        return tops_m[p]

    tops = 0
    h = m[p[1]][p[0]]
    if h == 9:
        return 1

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        np = (p[0] + dx, p[1] + dy)
        if in_bounds(np, m) and m[np[1]][np[0]] == h + 1:
            tops += find_tops2(np, m, tops_m)
    tops_m[p] = tops
    return tops


def parse_data(data):
    rows = data.split('\n')
    return rows
