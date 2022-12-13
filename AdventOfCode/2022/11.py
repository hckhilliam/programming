from collections import defaultdict, deque
import functools
import math
import re
import heapq


class Monkey(object):
    def __init__(self, id, items, divide, should_multiply, operands, t_dir, f_dir):
        self.id = id
        self.items = items
        self.divide = divide
        self.should_multiply = should_multiply
        self.operands = operands
        self.t_dir = t_dir
        self.f_dir = f_dir
        self.inspected = 0


def parse_monkey(row):
    lines = row.split('\n')
    id = int(lines[0].split(' ')[-1][:-1])
    items = [int(i) for i in lines[1].split(': ')[-1].split(', ')]
    equation = lines[2].split(' = ')[-1].split(' ')
    should_multiply = equation[1] == '*'
    operands = [equation[0], equation[-1]]
    divide = int(lines[3].split(' ')[-1])
    t_dir = int(lines[4].split(' ')[-1])
    f_dir = int(lines[5].split(' ')[-1])
    return Monkey(id, items, divide, should_multiply, operands, t_dir, f_dir)


def calculate_monkey_business(monkeys):
    return math.prod(heapq.nlargest(2, [m.inspected for m in monkeys.values()]))


def part1(data):
    rows = parse_data(data)
    monkeys = [parse_monkey(r) for r in rows]
    monkeys = {m.id: m for m in monkeys}

    for _ in range(20):
        for i in range(len(monkeys)):
            m = monkeys[i]
            m.inspected += len(m.items)
            while m.items:
                worry = m.items.pop()
                operands = [
                    worry if o == 'old' else int(o)
                    for o in m.operands
                ]
                if m.should_multiply:
                    worry = operands[0] * operands[1]
                else:
                    worry = operands[0] + operands[1]
                worry //= 3
                if worry % m.divide == 0:
                    monkeys[m.t_dir].items.append(worry)
                else:
                    monkeys[m.f_dir].items.append(worry)

    return calculate_monkey_business(monkeys)



def part2(data):
    rows = parse_data(data)
    monkeys = [parse_monkey(r) for r in rows]
    monkeys = {m.id: m for m in monkeys}

    phew = math.prod([m.divide for m in monkeys.values()])
    for _ in range(10000):
        for i in range(len(monkeys)):
            m = monkeys[i]
            m.inspected += len(m.items)
            while m.items:
                worry = m.items.pop()
                operands = [
                    worry if o == 'old' else int(o)
                    for o in m.operands
                ]
                if m.should_multiply:
                    worry = operands[0] * operands[1]
                else:
                    worry = operands[0] + operands[1]
                worry %= phew
                if worry % m.divide == 0:
                    monkeys[m.t_dir].items.append(worry)
                else:
                    monkeys[m.f_dir].items.append(worry)

    return calculate_monkey_business(monkeys)


def parse_data(data):
    monkeys = data.split('\n\n')
    return monkeys
