from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    total_arrangements = 0
    for r in rows:
        a, key = r.split(' ')
        keys = [int(k) for k in key.split(',')]
        arrangements = get_arrangements(a, 0, keys, 0, {}, '')
        total_arrangements += arrangements

    return total_arrangements


def get_arrangements(a, curr_i, keys, next_key, cache, curr_str):
    cache_key = (curr_i, next_key)
    if cache_key in cache:
        return cache[(curr_i, next_key)]

    if next_key == len(keys):
        cache[cache_key] = int(not any(c == '#' for c in a[curr_i:]))
        return cache[cache_key]
    if curr_i == len(a):
        cache[cache_key] = 0
        return cache[cache_key]

    initial_c = a[curr_i]
    if initial_c == '.':
        cache[cache_key] = get_arrangements(a, curr_i + 1, keys, next_key, cache, curr_str + '.')
        return cache[cache_key]

    k = keys[next_key]
    arrangements = 0
    if initial_c == '?':
        arrangements = get_arrangements(a, curr_i + 1, keys, next_key, cache, curr_str + '.')

    if not can_create_key(a, curr_i, k):
        cache[cache_key] = arrangements
        return arrangements

    next_i = curr_i + k
    if next_i < len(a):
        next_ch = a[next_i]
        # If next ch is #, we can't do this arrangement.
        if next_ch != '#':
            arrangements += get_arrangements(a, next_i + 1, keys, next_key + 1, cache, curr_str + ('#' * k) + '.')
    else:
        arrangements += get_arrangements(a, next_i, keys, next_key + 1, cache, curr_str + ('#' * k))

    cache[cache_key] = arrangements
    return arrangements


def can_create_key(a, curr_i, k):
    for i in range(k):
        if curr_i + i >= len(a) or a[curr_i + i] not in {'#', '?'}:
            return False
    return True


def part2(data):
    rows = parse_data(data)
    total_arrangements = 0
    for r in rows:
        a, key = r.split(' ')
        keys = [int(k) for k in key.split(',')]
        a = '?'.join(a for _ in range(5))
        keys = keys * 5
        arrangements = get_arrangements(a, 0, keys, 0, {}, '')
        total_arrangements += arrangements

    return total_arrangements


def parse_data(data):
    rows = data.split('\n')
    return rows
