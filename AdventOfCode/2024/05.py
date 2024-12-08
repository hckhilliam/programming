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

    dependencies = defaultdict(set)
    i = 0
    while True:
        r = rows[i]
        if not r:
            break

        d, s = r.split('|')
        dependencies[int(s)].add(int(d))
        i += 1
    i += 1

    total = 0
    while i < len(rows):
        instructions = [int(n) for n in rows[i].split(',')]
        if is_ordered(instructions, dependencies):
            total += instructions[len(instructions) // 2]
        i += 1

    return total


def is_ordered(instructions, dependencies):
    all_instructions = set(instructions)
    printed = set()
    for page in instructions:
        if not is_correct(page, printed, all_instructions, dependencies):
            return False
        printed.add(page)
    return True


def is_correct(page, printed, all_instructions, dependencies):
    for d in dependencies[page]:
        if d in all_instructions and d not in printed:
            return False
    return True


def part2(data):
    rows = parse_data(data)

    dependencies = defaultdict(set)
    i = 0
    while True:
        r = rows[i]
        if not r:
            break

        d, s = r.split('|')
        dependencies[int(s)].add(int(d))
        i += 1
    i += 1

    total = 0
    while i < len(rows):
        instructions = [int(n) for n in rows[i].split(',')]
        if not is_ordered(instructions, dependencies):
            ordered = order(instructions, dependencies)
            total += ordered[len(ordered) // 2]
        i += 1

    return total


def order(instructions, dependencies):
    all_instructions = set(instructions)
    dep_g = defaultdict(set)
    r_dep_g = defaultdict(set)

    no_deps = []
    for i in instructions:
        deps = dependencies[i] & all_instructions
        dep_g[i] = deps
        for d in deps:
            r_dep_g[d].add(i)
        if not deps:
            no_deps.append(i)

    order = []
    while no_deps:
        d = no_deps.pop()
        order.append(d)
        for rd in r_dep_g[d]:
            deps = dep_g[rd]
            deps.remove(d)
            if not deps:
                no_deps.append(rd)

    return order


def parse_data(data):
    rows = data.split('\n')
    return rows
