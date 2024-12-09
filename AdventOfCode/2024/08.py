from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array, in_bounds
import sys

debug = False


def part1(data):
    rows = parse_data(data)
    f_map = defaultdict(list)

    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == '.':
                continue

            f_map[c].append((x, y))

    antinodes = set()
    for positions in f_map.values():
        for i, p1 in enumerate(positions):
            for j in range(i + 1, len(positions)):
                p2 = positions[j]
                diff = (p1[0] - p2[0], p1[1] - p2[1])
                np1 = (p1[0] + diff[0], p1[1] + diff[1])
                if in_bounds(np1, rows):
                    antinodes.add(np1)
                np2 = (p2[0] - diff[0], p2[1] - diff[1])
                if in_bounds(np2, rows):
                    antinodes.add(np2)

    return len(antinodes)

def part2(data):
    rows = parse_data(data)
    f_map = defaultdict(list)

    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            if c == '.':
                continue

            f_map[c].append((x, y))

    antinodes = set()
    for positions in f_map.values():
        for i, p1 in enumerate(positions):
            antinodes.add(p1)
            for j in range(i + 1, len(positions)):
                p2 = positions[j]
                diff = (p1[0] - p2[0], p1[1] - p2[1])

                curr_p = p1
                while True:
                    np = (curr_p[0] + diff[0], curr_p[1] + diff[1])
                    if not in_bounds(np, rows):
                        break
                    antinodes.add(np)
                    curr_p = np

                curr_p = p2
                while True:
                    np = (curr_p[0] - diff[0], curr_p[1] - diff[1])
                    if not in_bounds(np, rows):
                        break
                    antinodes.add(np)
                    curr_p = np

    return len(antinodes)


def parse_data(data):
    rows = data.split('\n')
    return rows
