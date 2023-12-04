from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    total = 0
    for r in rows:
        _, numbers = r.split(': ')
        winning, yours = numbers.split('|')
        winning = set(winning.strip().split(' '))
        if '' in winning:
            winning.remove('')
        yours = set(yours.strip().split(' '))
        if '' in yours:
            yours.remove('')
        total_won = len(winning.intersection(yours))
        if total_won:
            total += pow(2, total_won - 1)
    return total


def part2(data):
    rows = parse_data(data)
    total_cards = defaultdict(int)

    for i, r in enumerate(rows):
        total_cards[i + 1] += 1
        num_cards = total_cards[i + 1]
        _, numbers = r.split(': ')
        winning, yours = numbers.split('|')
        winning = set(winning.strip().split(' '))
        if '' in winning:
            winning.remove('')
        yours = set(yours.strip().split(' '))
        if '' in yours:
            yours.remove('')
        total_won = len(winning.intersection(yours))
        for j in range(1, total_won + 1):
            total_cards[i + j + 1] += num_cards
    return sum(total_cards.values())


def parse_data(data):
    rows = data.split('\n')
    return rows
