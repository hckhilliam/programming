from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    lines = parse_data(data)
    points = defaultdict(int)

    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
    return len([v for v in points.values() if v > 1])


def part2(data):
    lines = parse_data(data)
    points = defaultdict(int)

    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(x, y1)] += 1
        else:
            dy = 1 if y2 - y1 > 0 else -1
            dx = 1 if x2 - x1 > 0 else -1
            while x1 != x2 and y1 != y2:
                points[(x1, y1)] += 1
                x1 += dx
                y1 += dy
            points[(x1, y1)] += 1
    return len([v for v in points.values() if v > 1])


def parse_data(data):
    rows = data.split('\n')
    lines = []
    for r in rows:
        p1, p2 = r.split(' -> ')
        lines.append(([int(p) for p in p1.split(',')], [int(p) for p in p2.split(',')]))
    return lines
