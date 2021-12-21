from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    p1, p2 = parse_data(data)
    p1_score = 0
    p2_score = 0
    i = 0
    rolls = 0
    while True:
        rolls, i = incr_i(rolls, i)
        total = i
        for _ in range(2):
            rolls, i = incr_i(rolls, i)
            total += i
        p1 = add(p1, total)
        p1_score += p1
        if p1_score >= 1000:
            return p2_score * rolls

        rolls, i = incr_i(rolls, i)
        total = i
        for _ in range(2):
            rolls, i = incr_i(rolls, i)
            total += i
        p2 = add(p2, total)
        p2_score += p2
        if p2_score >= 1000:
            return p1_score * rolls


def add(p, i):
    pp = (p + i) % 10
    if pp == 0:
        return 10
    return pp


def incr_i(rolls, i):
    ii = (i + 1) % 100
    if ii == 0:
        return rolls + 1, 100
    return rolls + 1, ii


def part2(data):
    p1, p2 = parse_data(data)
    cache = {}
    p1_wins = find_wins(p1, p2, 0, 0, 21, p1_first=True, cache=cache)
    p2_wins = find_wins(p2, p1, 0, 0, 21, p1_first=False, cache=cache)
    return max(p1_wins, p2_wins)


def find_wins(p1, p2, p1_score, p2_score, goal, p1_first, cache):
    cache_key = (p1, p2, p1_score, p2_score, p1_first)
    if cache_key in cache:
        return cache[cache_key]
    if p1_score >= goal:
        return 1
    elif p2_score >= goal:
        return 0

    counts = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }
    wins = 0
    if p1_first:
        for i in range(3, 10):
            np = add(p1, i)
            wins += counts[i] * find_wins(
                np, p2, p1_score + np, p2_score, goal,
                p1_first=False, cache=cache
            )
    else:
        for i in range(3, 10):
            np = add(p2, i)
            wins += counts[i] * find_wins(
                p1, np, p1_score, p2_score + np, goal,
                p1_first=True, cache=cache
            )

    cache[cache_key] = wins
    return wins


def parse_data(data):
    rows = data.split('\n')
    return int(rows[0].split(' ')[-1]), int(rows[1].split(' ')[-1])
