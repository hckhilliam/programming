from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    stacks, instructions = parse_data(data)
    for i in instructions:
        _, amount, _, source, _, dest = i.split(' ')
        amount = int(amount)
        source = int(source)
        dest = int(dest)

        for i in range(amount):
            l = stacks[source].pop()
            stacks[dest].append(l)

    sorted_keys = sorted(stacks.keys())
    final = ''
    for k in sorted_keys:
        final += stacks[k][-1]
    return final


def part2(data):
    stacks, instructions = parse_data(data)
    for i in instructions:
        _, amount, _, source, _, dest = i.split(' ')
        amount = int(amount)
        source = int(source)
        dest = int(dest)

        temp = []
        for i in range(amount):
            l = stacks[source].pop()
            temp.append(l)
        while temp:
            stacks[dest].append(temp.pop())

    sorted_keys = sorted(stacks.keys())
    final = ''
    for k in sorted_keys:
        final += stacks[k][-1]
    return final


def parse_data(data):
    m, instructions = data.split('\n\n')
    item_length = 4
    stacks = defaultdict(deque)
    for r in m.split('\n'):
        i = 0
        stack_num = 1
        while i < len(r):
            bound = i + item_length
            for c in range(i, bound):
                if c < len(r) and r[c].isalpha():
                    stacks[stack_num].appendleft(r[c])
                    break
            i = bound
            stack_num += 1

    return stacks, instructions.split('\n')
