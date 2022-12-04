from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    contained = 0
    for r in rows:
        first, second = r.split(',')
        s1, e1 = [int(n) for n in first.split('-')]
        s2, e2 = [int(n) for n in second.split('-')]
        if (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
            contained += 1

    return contained


def part2(data):
    rows = parse_data(data)

    overlapped = 0
    for r in rows:
        first, second = r.split(',')
        s1, e1 = [int(n) for n in first.split('-')]
        s2, e2 = [int(n) for n in second.split('-')]
        if not (e1 < s2 or s1 > e2):
            overlapped += 1

    return overlapped


def parse_data(data):
    rows = data.split('\n')
    return rows
