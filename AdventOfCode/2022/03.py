from collections import defaultdict, deque
import functools
import math
import re


def get_priority(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def part1(data):
    rows = parse_data(data)

    priority = 0
    for r in rows:
        fs = set()
        bs = set()
        for i in range(int(len(r)/2)):
            f = r[i]
            b = r[-i - 1]
            if f in bs:
                priority += get_priority(f)
                break
            else:
                fs.add(f)
            if b in fs:
                priority += get_priority(b)
                break
            else:
                bs.add(b)
    return priority


def part2(data):
    rows = parse_data(data)

    priority = 0
    i = 0
    while i < len(rows):
        groups = rows[i:i + 3]
        for c in groups[0]:
            if c in groups[1] and c in groups[2]:
                priority += get_priority(c)
                break
        i += 3
    return priority


def parse_data(data):
    rows = data.split('\n')
    return rows
