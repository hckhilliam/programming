from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array
import sys

debug = False


def part1(data):
    rows = parse_data(data)
    l1 = []
    l2 = []
    for r in rows:
        splits = r.split(' ')
        l1.append(int(splits[0]))
        l2.append(int(splits[-1]))

    l1.sort()
    l2.sort()

    td = 0
    for i in range(len(rows)):
        td += abs(l1[i] - l2[i])

    return td


def part2(data):
    rows = parse_data(data)
    l1 = []
    l2 = []
    l2c = defaultdict(int)
    for r in rows:
        splits = r.split(' ')
        l1.append(int(splits[0]))
        l2.append(int(splits[-1]))
        l2c[l2[-1]] += 1

    ts = 0
    for l in l1:
        ts += l * l2c[l]

    return ts


def parse_data(data):
    rows = data.split('\n')
    return rows
