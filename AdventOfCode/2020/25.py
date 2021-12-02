from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    ckey = int(rows[0])
    dkey = int(rows[1])

    i = 0
    v = 1
    s = 7
    while v != ckey:
        v = (s * v) % 20201227
        i += 1

    s = dkey
    v = 1
    for j in range(i):
        v = (s * v) % 20201227
    return v


def part2(data):
    rows = parse_data(data)


def parse_data(data):
    rows = data.split('\n')
    return rows
