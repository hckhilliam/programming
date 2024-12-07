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
    reports = [r.split(' ') for r in rows]

    safes = 0
    for report in reports:
        if is_safe(report):
            safes += 1

    return safes


def part2(data):
    rows = parse_data(data)
    reports = [r.split(' ') for r in rows]

    safes = 0
    for report in reports:
        unsafe_i = is_safe(report)
        if unsafe_i is True:
            safes += 1
        elif (is_safe(report[0:unsafe_i] + report[unsafe_i + 1:len(report)]) is True or
            is_safe(report[0:unsafe_i - 1] + report[unsafe_i:len(report)]) is True):
            safes += 1

    return safes


def is_safe(report):
    ireport = [int(r) for r in report]
    r = ireport[0]
    rr = ireport[1]
    is_inc = rr - r > 0
    i = 1
    while i < len(ireport):
        rr = ireport[i]
        diff = rr - r
        abs_d = abs(diff)
        if abs_d > 3 or abs_d < 1 or (is_inc and diff < 0) or (not is_inc and diff > 0):
            return i
        i += 1
        r = rr
    return True


def parse_data(data):
    rows = data.split('\n')
    return rows
