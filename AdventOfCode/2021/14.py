from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    start, patterns = parse_data(data)
    for i in range(10):
        start = find_new_start(start, patterns)
    counts = defaultdict(int)
    for c in start:
        counts[c] += 1
    pairs = [(k, v) for k, v in counts.items()]
    pairs.sort(key=lambda x: x[1])
    return pairs[-1][1] - pairs[0][1]


def find_new_start(start, patterns):
    prev = start[0]
    curr_str = start[0]
    for i in range(1, len(start)):
        pair = prev + start[i]
        if pair in patterns:
            curr_str += patterns[pair]
        curr_str += start[i]
        prev = start[i]
    return curr_str


def part2(data):
    start, patterns = parse_data(data)
    cache = dict()
    total_counts = defaultdict(int)
    for k in start:
        total_counts[k] += 1
    for i in range(len(start) - 1):
        k = (start[i] + start[i + 1], 40)
        if k not in cache:
            build_counts(k[0], patterns, cache, k[1])
        counts = cache[k]
        for ch, v in counts.items():
            total_counts[ch] += v
    pairs = [(ch, c) for ch, c in total_counts.items()]
    pairs.sort(key=lambda x: x[1])
    return pairs[-1][1] - pairs[0][1]


def build_counts(pair, patterns, cache, steps):
    if (pair, steps) in cache:
        return cache[(pair, steps)]
    elif pair not in patterns:
        cache[(pair, steps)] = defaultdict(int)
        return cache[(pair, steps)]
    elif steps == 1:
        res = defaultdict(int, { patterns[pair]: 1 })
        cache[(pair, steps)] = res
        return res


    counts1 = build_counts(pair[0] + patterns[pair], patterns, cache, steps - 1)
    counts2 = build_counts(patterns[pair] + pair[1], patterns, cache, steps - 1)
    total_counts = defaultdict(int, { patterns[pair]: 1 })
    for k, v in counts1.items():
        total_counts[k] += v
    for k, v in counts2.items():
        total_counts[k] += v
    cache[(pair, steps)] = total_counts
    return total_counts


def parse_data(data):
    rows = data.split('\n')
    start = rows[0]
    patterns = {}
    for i in range(2, len(rows)):
        s, r = rows[i].split(' -> ')
        patterns[s] = r
    return start, patterns
