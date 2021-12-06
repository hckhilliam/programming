from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    fish_spawns = parse_data(data)
    return compute_fish(80, fish_spawns)


def part2(data):
    fish_spawns = parse_data(data)
    return compute_fish(256, fish_spawns)


def compute_fish(days, fish_spawns):
    total_fish = len(fish_spawns)
    new_fish = defaultdict(int)
    for s in fish_spawns:
        new_fish[s + 1] += 1

    for i in range(1, days + 1):
        new_borns = new_fish.get(i)
        if not new_borns:
            continue
        total_fish += new_borns
        new_fish[i + 7] += new_borns
        new_fish[i + 9] += new_borns

    return total_fish


def parse_data(data):
    fish_spawns = [int(s) for s in data.split(',')]
    return fish_spawns
