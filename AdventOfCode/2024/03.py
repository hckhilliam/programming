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

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    total = 0
    for row in rows:
        statements = re.findall(pattern, row)
        for l, r in statements:
            total += int(l) * int(r)

    return total


def part2(data):
    rows = parse_data(data)
    s = ''
    for r in rows:
        s += r

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    next_dont = s.find('don\'t()')
    current_ind = 0
    do = True
    while next_dont != -1:
        statements = re.findall(pattern, s[current_ind:current_ind + next_dont])
        for l, r in statements:
            total += int(l) * int(r)
        current_ind += next_dont + 7
        next_do = s[current_ind:].find('do()')
        if next_do == -1:
            do = False
            break
        current_ind += 4 + next_do
        next_dont = s[current_ind:].find('don\'t()')
    if do:
        statements = re.findall(pattern, s[current_ind:])
        for l, r in statements:
            total += int(l) * int(r)

    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
