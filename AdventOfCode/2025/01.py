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

    pw = 0
    dial = 50
    for r in rows:
        d = r[0]
        n = int(r[1:])

        op = 1
        if d == 'L':
            op = -1
        dial = (dial + (op * n)) % 100

        if dial == 0:
            pw += 1

    return pw


def part2(data):
    rows = parse_data(data)

    pw = 0
    dial = 50
    for r in rows:
        d = r[0]
        n = int(r[1:])
        roundabouts = n // 100
        n %= 100
        pw += roundabouts

        op = 1
        if d == 'L':
            op = -1
        pd = dial
        dial += (op * n)
        
        if (pd > 0 and dial <= 0) or dial > 99:
            pw += 1
        dial %= 100

    return pw


def parse_data(data):
    rows = data.split('\n')
    return rows
