from collections import defaultdict
import functools
import math


def part1(data):
    rows = parse_data(data)
    details = defaultdict(list)
    i = 0
    while rows[i] != '':
        parts = rows[i].split(':')
        name = parts[0]
        pp = parts[1].split(' or ')
        first_int = pp[0].strip().split('-')
        second_int = pp[1].strip().split('-')
        details[name].append((int(first_int[0]), int(first_int[1])))
        details[name].append((int(second_int[0]), int(second_int[1])))
        i += 1
    i += 5  # skip your ticket stuff

    error_rate = 0
    while i < len(rows):
        parts = [int(p) for p in rows[i].split(',')]
        for p in parts:
            valid = False
            for v in details.values():
                for interval in v:
                    if interval[0] <= p <= interval[1]:
                        valid = True
                        break
                if valid:
                    break
            if not valid:
                error_rate += p
        i += 1
    return error_rate


def part2(data):
    rows = parse_data(data)
    details = defaultdict(list)
    i = 0
    while rows[i] != '':
        parts = rows[i].split(':')
        name = parts[0]
        pp = parts[1].split(' or ')
        first_int = pp[0].strip().split('-')
        second_int = pp[1].strip().split('-')
        details[name].append((int(first_int[0]), int(first_int[1])))
        details[name].append((int(second_int[0]), int(second_int[1])))
        i += 1
    i += 2
    me = [int(p) for p in rows[i].split(',')]
    i += 3

    valids = []
    while i < len(rows):
        parts = [int(p) for p in rows[i].split(',')]
        v1 = True
        for p in parts:
            v2 = False
            for v in details.values():
                v3 = False
                for interval in v:
                    if interval[0] <= p <= interval[1]:
                        v3 = True
                        break
                if v3:
                    v2 = True
                    break
            if not v2:
                v1 = False
                break
        if v1:
            valids.append(parts)
        i += 1

    possibilities = defaultdict(set)
    for i in range(len(details)):
        for desc, intervals in details.items():
            valid = True
            for va in valids:
                cv = False
                for interval in intervals:
                    if interval[0] <= va[i] <= interval[1]:
                        cv = True
                        break
                if not cv:
                    valid = False
                    break
            if valid:
                possibilities[desc].add(i)

    i = 1
    pos = {}
    used = set()
    while i <= len(details):
        for k, v in possibilities.items():
            if len(v) == i:
                num = list(v - used)[0]
                pos[num] = k
                used.add(num)
                break
        i += 1

    ret = 1
    for i in range(len(me)):
        if pos[i].startswith('departure'):
            ret *= me[i]
    return ret


def parse_data(data):
    rows = data.split('\n')
    return rows
