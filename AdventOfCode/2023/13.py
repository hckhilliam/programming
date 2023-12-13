from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    patterns = []
    curr_pattern = []
    for r in rows:
        if r:
            curr_pattern.append(r)
        else:
            patterns.append(curr_pattern)
            curr_pattern = []
    patterns.append(curr_pattern)

    s = 0
    for p in patterns:
        s += find_reflection_line(p)
    return s


def find_reflection_line(p):
    # Horizontal
    for i in range(1, len(p)):
        if is_perfect_reflection_h(p, i):
            return i * 100

    # Vertical
    for i in range(1, len(p[0])):
        if is_perfect_reflection_v(p, i):
            return i


def is_perfect_reflection_h(p, i):
    opp = i - 1
    while opp >= 0 and i < len(p):
        for j in range(len(p[0])):
            if p[opp][j] != p[i][j]:
                return False
        opp -= 1
        i += 1
    return True


def is_perfect_reflection_v(p, i):
    opp = i - 1
    while opp >= 0 and i < len(p[0]):
        for j in range(len(p)):
            if p[j][opp] != p[j][i]:
                return False
        opp -= 1
        i += 1
    return True


def part2(data):
    rows = parse_data(data)
    patterns = []
    curr_pattern = []
    for r in rows:
        if r:
            curr_pattern.append(r)
        else:
            patterns.append(curr_pattern)
            curr_pattern = []
    patterns.append(curr_pattern)

    s = 0
    for p in patterns:
        s += find_reflection_line_2(p)
    return s


def find_reflection_line_2(p):
    # Horizontal
    for i in range(1, len(p)):
        if is_smudge_reflection_h_2(p, i):
            return i * 100

    # Vertical
    for i in range(1, len(p[0])):
        if is_smudge_reflection_v_2(p, i):
            return i


def is_smudge_reflection_h_2(p, i):
    opp = i - 1
    found_smudge = False
    while opp >= 0 and i < len(p):
        for j in range(len(p[0])):
            if p[opp][j] != p[i][j]:
                if found_smudge:
                    return False
                else:
                    found_smudge = True
        opp -= 1
        i += 1
    return found_smudge


def is_smudge_reflection_v_2(p, i):
    opp = i - 1
    found_smudge = False
    while opp >= 0 and i < len(p[0]):
        for j in range(len(p)):
            if p[j][opp] != p[j][i]:
                if found_smudge:
                    return False
                else:
                    found_smudge = True
        opp -= 1
        i += 1
    return found_smudge


def parse_data(data):
    rows = data.split('\n')
    return rows
