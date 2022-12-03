from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    scores = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    win_map = {
        'X': {
            'A': 3,
            'B': 0,
            'C': 6
        },
        'Y': {
            'A': 6,
            'B': 3,
            'C': 0
        },
        'Z': {
            'A': 0,
            'B': 6,
            'C': 3
        }
    }

    total_score = 0
    for r in rows:
        opp, me = r.split(' ')
        total_score += scores[me] + win_map[me][opp]
    return total_score


def part2(data):
    rows = parse_data(data)

    scores = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    win_map = {
        'X': {
            'A': 3,
            'B': 1,
            'C': 2
        },
        'Y': {
            'A': 1,
            'B': 2,
            'C': 3
        },
        'Z': {
            'A': 2,
            'B': 3,
            'C': 1
        }
    }

    total_score = 0
    for r in rows:
        opp, me = r.split(' ')
        total_score += scores[me] + win_map[me][opp]
    return total_score


def parse_data(data):
    rows = data.split('\n')
    return rows
