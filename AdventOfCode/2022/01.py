from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)

    most_calories = 0

    curr_calories = 0
    for r in rows:
        if r == '':
            most_calories = max(most_calories, curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(r)
    return most_calories


def part2(data):
    rows = parse_data(data)

    calories = []
    curr_calories = 0
    for r in rows:
        if r == '':
            calories.append(curr_calories)
            curr_calories = 0
        else:
            curr_calories += int(r)
    calories.sort(reverse=True)
    return sum(calories[:3])


def parse_data(data):
    rows = data.split('\n')
    return rows
