from collections import defaultdict, deque
import functools
import math
import re
import heapq
from math import gcd


def part1(data):
    rows = parse_data(data)
    instruction = rows[0].strip()

    m = {}
    for r in rows[2:]:
        k, parts = r.split(' = ')
        pp = parts.split(', ')
        m[k] = {
            'L': pp[0].strip()[1:],
            'R': pp[1].strip()[:-1]
        }

    curr = 'AAA'

    steps = 0
    while curr != 'ZZZ':
        for c in instruction:
            mm = m[curr]
            steps += 1
            curr = mm[c]
            if curr == 'ZZZ':
                break
    return steps


def part2(data):
    rows = parse_data(data)
    instruction = rows[0].strip()

    m = {}
    starts = set()
    for r in rows[2:]:
        k, parts = r.split(' = ')
        pp = parts.split(', ')
        m[k] = {
            'L': pp[0].strip()[1:],
            'R': pp[1].strip()[:-1]
        }
        if k.endswith('A'):
            starts.add(k)

    cycle_map = {}
    for start in starts:
        initial_steps, cycle_steps = get_all_steps(start, m, instruction)
        cycle_map[start] = {
            'initial_steps': initial_steps,
            'cycle_steps': cycle_steps,
            'done_initial': False,
            'i': 1
        }
    print(cycle_map)

    # Since input all has only 1 step for cycle steps, we can just do this.
    lcm = 1
    for c in map(lambda c: c['cycle_steps'][0], cycle_map.values()):
        lcm = lcm * c // gcd(lcm, c)
    return lcm

    # Brute force approach. Too slow.
    # all_steps = [(c['initial_steps'][0], k) for k, c in cycle_map.items()]
    # heapq.heapify(all_steps)
    # while not all_equal(all_steps):
    #     min_steps, k = heapq.heappop(all_steps)
    #     c = cycle_map[k]
    #     next_step = get_next_step(min_steps, c)
    #     heapq.heappush(all_steps, (next_step, k))
    # return all_steps[0][0]





def get_all_steps(start, m, instruction):
    visited_z = set()
    curr = start
    initial_steps = []
    steps = 0
    ins_ind = 0
    # Find first cycle.
    while curr not in visited_z:
        if curr.endswith('Z'):
            visited_z.add(curr)
        c = instruction[ins_ind]
        mm = m[curr]
        steps += 1
        curr = mm[c]
        if curr.endswith('Z'):
            initial_steps.append(steps)
        ins_ind = (ins_ind + 1) % len(instruction)
    steps = 0
    cycle_steps = []
    # Keep adding to repeated cycle to ensure.
    visited_z = set()
    while curr not in visited_z:
        if curr.endswith('Z'):
            visited_z.add(curr)
        c = instruction[ins_ind]
        mm = m[curr]
        steps += 1
        curr = mm[c]
        if curr.endswith('Z'):
            cycle_steps.append(steps)
        ins_ind = (ins_ind + 1) % len(instruction)
    return initial_steps, cycle_steps


def all_equal(all_steps):
    if len(all_steps) <= 1:
        return True
    first = all_steps[0][0]
    for s, _ in all_steps[1:]:
        if s != first:
            return False
    return True


def get_next_step(min_steps, c):
    if not c['done_initial']:
        next_step = c['initial_steps'][c['i']]
        c['i'] += 1
        if c['i'] == len(c['initial_steps']):
            c['done_initial'] = True
            c['i'] = 0
        return next_step
    else:
        next_step = min_steps + c['cycle_steps'][c['i']]
        c['i'] = (c['i'] + 1) % len(c['cycle_steps'])
        return next_step


def parse_data(data):
    rows = data.split('\n')
    return rows
