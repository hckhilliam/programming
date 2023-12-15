from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    parts = rows[0].split(',')
    total = 0
    for p in parts:
        total += get_hash(p)
    return total


def get_hash(p):
    hash = 0
    for c in p:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


def part2(data):
    rows = parse_data(data)

    label_values = {}
    label_hashes = {}
    m = defaultdict(list)
    parts = rows[0].split(',')
    for p in parts:
        v = None
        if '=' in p:
            h, v = p.split('=')
            v = int(v)
            is_equals = True
        else:
            h = p[:-1]
            is_equals = False

        if h not in label_hashes:
            label_hashes[h] = get_hash(h)
        hash = label_hashes[h]

        box = m[hash]
        if is_equals:
            if h not in label_values:
                box.append(h)
            label_values[h] = v
        else:
            if h in label_values:
                del label_values[h]
                box.remove(h)

    total = 0
    for l, v in label_values.items():
        hash = label_hashes[l]
        box = m[hash]
        i = 0
        while i < len(box):
            if box[i] == l:
                break
            i += 1
        i += 1
        power = (1 + hash) * i * v
        total += power
    return total


def parse_data(data):
    rows = data.split('\n')
    return rows
