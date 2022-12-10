from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    r = rows[0]
    window = deque(r[:4])
    i = 4
    while len(set(window)) < 4:
        window.append(r[i])
        i += 1
        window.popleft()
    return i


def part2(data):
    rows = parse_data(data)

    r = rows[0]
    window = deque(r[:14])
    i = 4
    while len(set(window)) < 14:
        window.append(r[i])
        i += 1
        window.popleft()
    return i


def parse_data(data):
    rows = data.split('\n')
    return rows
