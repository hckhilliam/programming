from collections import defaultdict, deque
import functools
import math
import re
import json


def compare_packets(p1, p2):
    if type(p1) == list and type(p2) != list:
        p2 = [p2]
        # return not p1 or compare_packets(p1[0], p2)
    elif type(p2) == list and type(p1) != list:
        p1 = [p1]

    if type(p1) != list:
        if p1 < p2:
            return -1
        elif p1 == p2:
            return 0
        return 1

    i = 0
    j = 0
    while i < len(p1) and j < len(p2):
        pp1 = p1[i]
        pp2 = p2[j]

        v = compare_packets(pp1, pp2)
        if v != 0:
            return v

        i += 1
        j += 1

    if len(p1) < len(p2):
        return -1
    elif len(p1) == len(p2):
        return 0
    return 1


def part1(data):
    rows = parse_data(data)

    total_order = 0
    for i, r in enumerate(rows):
        p1, p2 = r.split('\n')
        p1 = json.loads(p1)
        p2 = json.loads(p2)

        if compare_packets(p1, p2) == -1:
            total_order += i + 1
    return total_order


def part2(data):
    rows = parse_data(data)
    packets = [[[2]], [[6]]]
    for r in rows:
        p1, p2 = r.split('\n')
        packets.append(json.loads(p1))
        packets.append(json.loads(p2))

    packets.sort(key=functools.cmp_to_key(compare_packets))

    pos = []
    for i, p in enumerate(packets):
        if p == [[2]] or p == [[6]]:
            pos.append(i + 1)
    return math.prod(pos)



def parse_data(data):
    rows = data.split('\n\n')
    return rows
