from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    times = [int(t.strip()) for t in rows[0].split(':')[-1].split(' ') if t]
    distances = [int(d.strip()) for d in rows[1].split(':')[-1].split(' ') if d]

    all_ways = []
    for i in range(len(times)):
        time = times[i]
        m_distance = distances[i]
        ways = 0
        for j in range(1, time):
            if greater(m_distance, time, j):
                ways += 1
        all_ways.append(ways)

    return math.prod(all_ways)


def greater(m_d, t, j):
    time_left = t - j
    if time_left * j > m_d:
        return True
    return False


def part2(data):
    rows = parse_data(data)
    time = int(rows[0].split(':')[-1].replace(' ', ''))
    distance = int(rows[1].split(':')[-1].replace(' ', ''))
    x1 = math.ceil((-time + math.sqrt(time * time - 4 * distance)) / -2)
    x2 = math.ceil((-time - math.sqrt(time * time - 4 * distance)) / -2)
    return x2 - x1


def parse_data(data):
    rows = data.split('\n')
    return rows
