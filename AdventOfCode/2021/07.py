from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    mm = max(rows)
    min_d = None
    for i in range(mm):
        d = 0
        for r in rows:
            d += abs(i - r)
        if not min_d:
            min_d = d
        elif d < min_d:
            min_d = d
    return min_d


def part2(data):
    rows = parse_data(data)
    mm = max(rows)
    min_d = None
    for i in range(mm):
        d = 0
        for r in rows:
            n = abs(i - r)
            d += n * (n + 1) / 2
        if not min_d:
            min_d = d
        elif d < min_d:
            min_d = d
    return min_d


def parse_data(data):
    rows = [int(d) for d in data.split(',')]
    return rows
