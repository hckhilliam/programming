from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, to_int_array, in_bounds, DIRS, O_DIRS, P
import sys

debug = False


def part1(data):
    rows = parse_data(data)

    stones = [int(n) for n in rows[0].split(' ')]

    total_stones = 0
    cache = {} # (num, blinks_left) to total stones
    for s in stones:
        total_stones += count_stones(s, 25, cache)
    return total_stones


def count_stones(s, blinks_left, cache):
    k = (s, blinks_left)
    if k in cache:
        return cache[k]

    ss = str(s)
    if blinks_left == 0:
        cache[k] = 1
    elif s == 0:
        cache[k] = count_stones(1, blinks_left - 1, cache)
    elif len(ss) % 2 == 0:
        h = len(ss) // 2
        cache[k] = count_stones(int(ss[:h]), blinks_left - 1, cache) + count_stones(int(ss[h:]), blinks_left - 1, cache)
    else:
        cache[k] = count_stones(s * 2024, blinks_left - 1, cache)
    return cache[k]


def part2(data):
    rows = parse_data(data)

    stones = [int(n) for n in rows[0].split(' ')]

    total_stones = 0
    cache = {} # (num, blinks_left) to total stones
    for s in stones:
        total_stones += count_stones(s, 75, cache)
    return total_stones


def parse_data(data):
    rows = data.split('\n')
    return rows
