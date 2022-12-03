from collections import defaultdict, deque
import functools
import math
import re


class Program(object):
    def __init__(self, shift, add_x, add_y):
        self.shift = shift
        self.add_x = add_x
        self.add_y = add_y


def part1(data):
    programs = parse_data(data)
    a = [9 for _ in range(14)]
    z = []
    last_bit_ind = 0
    last_bit = 0
    for i, p in enumerate(programs):
        if p.shift:
            z.append((last_bit_ind, last_bit))
            last_bit_ind = i
            last_bit = a[i] + p.add_y
        else:
            # shift right
            while p.add_x + last_bit != a[i]:
                a[i] -= 1
                if a[i] == 0:
                    a[i] = 9
                    a[last_bit_ind] -= 1
                    last_bit = a[last_bit_ind] + programs[last_bit_ind].add_y
            last_bit_ind, last_bit = z.pop()
    print(evaluate(data.split('\n'), a))
    return ''.join([str(c) for c in a])


def part2(data):
    programs = parse_data(data)
    a = [1 for _ in range(14)]
    z = []
    last_bit_ind = 0
    last_bit = 0
    for i, p in enumerate(programs):
        if p.shift:
            z.append((last_bit_ind, last_bit))
            last_bit_ind = i
            last_bit = a[i] + p.add_y
        else:
            # shift right
            while p.add_x + last_bit != a[i]:
                a[i] += 1
                if a[i] == 10:
                    a[i] = 1
                    a[last_bit_ind] += 1
                    last_bit = a[last_bit_ind] + programs[last_bit_ind].add_y
            last_bit_ind, last_bit = z.pop()
    print(evaluate(data.split('\n'), a))
    return ''.join([str(c) for c in a])


def evaluate(rows, a):
    variables = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    ai = 0
    for r in rows:
        instruction = r.split(' ')
        cmd = instruction[0]
        p = instruction[1]
        v2 = None
        if len(instruction) == 3:
            v2 = variables.get(instruction[2])
            if v2 is None:
                v2 = int(instruction[2])
        if cmd == 'inp':
            variables[p] = a[ai]
            ai += 1
        elif cmd == 'mul':
            variables[p] *= v2
        elif cmd == 'div':
            variables[p] //= v2
        elif cmd == 'add':
            variables[p] += v2
        elif cmd == 'mod':
            variables[p] %= v2
        elif cmd == 'eql':
            variables[p] = int(variables[p] == v2)
    return variables['z']


def parse_data(data):
    rows = data.split('\n')
    start = 1
    program_lines = []
    while start < 252:
        program_lines.append((start, start + 17))
        start += 18

    programs = []
    for s, e in program_lines:
        instructions = rows[s:e]
        shift = instructions[3].split(' ')[-1] == '1'
        check = int(instructions[4].split(' ')[-1])
        add = int(instructions[14].split(' ')[-1])
        programs.append(Program(shift, check, add))

    return programs
