from collections import defaultdict, deque
import functools
import math
import re
from functools import cmp_to_key


def part1(data):
    rows = parse_data(data)
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1']
    ranks = {c: i for i, c in enumerate(cards)}
    hands = []
    for row in rows:
        hand, bid = row.split(' ')
        hands.append((hand, int(bid)))

    sorted_hands = sorted(hands, key=cmp_to_key(create_hand_cmp(ranks, get_rank)))
    total = 0
    for i, h in enumerate(sorted_hands):
        total += (i + 1) * h[1]
    return total


def create_hand_cmp(ranks, get_rank_v):
    def compare_hands(p1, p2):
        h1 = p1[0]
        h2 = p2[0]
        if h1 == h2:
            return 0
        r1 = get_rank_v(h1)
        r2 = get_rank_v(h2)
        if r1 > r2:
            return 1
        elif r2 > r1:
            return -1
        else:
            for i in range(5):
                c1 = h1[i]
                c2 = h2[i]
                # I reversed the map oops.
                if ranks[c1] < ranks[c2]:
                    return 1
                elif ranks[c2] < ranks[c1]:
                    return -1
        # never happen
        return 0
    return compare_hands


def get_rank(hand):
    counts = defaultdict(int)
    for h in hand:
        counts[h] += 1

    five = 0
    four = 0
    three = 0
    two = 0
    for v in counts.values():
        if v == 5:
            five += 1
        elif v == 4:
            four += 1
        elif v == 3:
            three += 1
        elif v == 2:
            two += 1

    if five:
        return 7
    elif four:
        return 6
    elif three and two:
        return 5
    elif three:
        return 4
    elif two >= 2:
        return 3
    elif two == 1:
        return 2
    return 1


def part2(data):
    rows = parse_data(data)
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'J']
    ranks = {c: i for i, c in enumerate(cards)}
    hands = []
    for row in rows:
        hand, bid = row.split(' ')
        hands.append((hand, int(bid)))

    sorted_hands = sorted(hands, key=cmp_to_key(create_hand_cmp(ranks, get_rank2)))
    total = 0
    for i, h in enumerate(sorted_hands):
        total += (i + 1) * h[1]
    return total


def get_rank2(hand):
    counts = defaultdict(int)
    for h in hand:
        counts[h] += 1

    five = 0
    four = 0
    three = 0
    two = 0
    for k, v in counts.items():
        if k == 'J':
            continue
        if v == 5:
            five += 1
        elif v == 4:
            four += 1
        elif v == 3:
            three += 1
        elif v == 2:
            two += 1

    wildcards = counts['J']
    if wildcards == 5:
        return 7

    if five:
        return 7
    elif four:
        return 7 if wildcards else 6
    elif three:
        if wildcards == 2:
            return 7
        elif wildcards:
            return 6
        elif two:
            return 5
        return 4
    elif two >= 2:
        if wildcards:
            return 5
        return 3
    elif two == 1:
        if wildcards == 3:
            return 7
        elif wildcards == 2:
            return 6
        elif wildcards:
            return 4
        return 2
    if wildcards == 4:
        return 7
    elif wildcards == 3:
        return 6
    elif wildcards == 2:
        return 4
    elif wildcards:
        return 2
    return 1


def parse_data(data):
    rows = data.split('\n')
    return rows
