from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array
import sys
import copy

debug = False


def part1(data):
    rows = parse_data(data)
    instructions = defaultdict(list)
    parts = []
    done_instructions = False
    for r in rows:
        if not r:
            done_instructions = True
            continue
        if not done_instructions:
            name, inst = r.split('{')
            inst = inst[:-1].split(',')
            instructions[name] = [parse_instruction(i) for i in inst]
        else:
            values = r[1:-1].split(',')
            part = {}
            for v in values:
                c, val = v.split('=')
                part[c] = int(val)
            parts.append(part)

    total = 0
    for p in parts:
        if accepted(p, instructions):
            if debug:
                print(p)
            total += sum(p.values())
    return total


def parse_instruction(i):
    if ':' not in i:
        return {
            'd': i
        }
    rule, d = i.split(':')
    return {
        'rule': rule,
        'd': d
    }


def accepted(p, instructions):
    x = p['x']
    m = p['m']
    a = p['a']
    s = p['s']
    w = 'in'
    while w not in {'R', 'A'}:
        if w == 'R':
            return False
        if w == 'A':
            return True
        wis = instructions[w]

        for i in wis:
            rule = i.get('rule')
            d = i.get('d')
            if not rule or eval(rule):
                w = d
                break
    return w == 'A'


def part2(data):
    rows = parse_data(data)
    instructions = defaultdict(list)
    for r in rows:
        if not r:
            break
        name, inst = r.split('{')
        inst = inst[:-1].split(',')
        instructions[name] = [parse_instruction(i) for i in inst]

    rules = {
        'x': {
            '>=': 1,
            '<': 4001,
        },
        'm': {
            '>=': 1,
            '<': 4001,
        },
        'a': {
            '>=': 1,
            '<': 4001,
        },
        's': {
            '>=': 1,
            '<': 4001,
        },
    }
    rules = get_paths('in', rules, instructions)

    intervals = [{
        'x': [r['x']['>='], r['x']['<']],
        'm': [r['m']['>='], r['m']['<']],
        'a': [r['a']['>='], r['a']['<']],
        's': [r['s']['>='], r['s']['<']],
    } for r in rules]
    # Sort by x.
    intervals.sort(key=lambda i: i['x'][0])

    total_combos = 0
    # Go through each interval and subtract overlapping intervals.
    for i in range(len(intervals)):
        interval = intervals[i]
        total_combos += get_combos(interval)
        for j in range(i + 1, len(intervals)):
            other = intervals[j]
            if interval['x'][1] <= other['x'][0]:
                break
            x = get_overlap(interval['x'], other['x'])
            m = get_overlap(interval['m'], other['m'])
            a = get_overlap(interval['a'], other['a'])
            s = get_overlap(interval['s'], other['s'])
            total_combos -= x * m * a * s

    return total_combos


def get_combos(interval):
    return functools.reduce(lambda a, b: a * b, [v[1] - v[0] for v in interval.values()])


def get_overlap(i1, i2):
    return max(min(i1[1], i2[1]) - max(i1[0], i2[0]), 0)


opp_map = {
    '>=': ('<', min),
    '<': ('>=', max),
}
def get_paths(i, curr_rule, instructions):
    rules = []
    wis = instructions[i]
    new_rule = copy.deepcopy(curr_rule)
    for idx in range(len(wis) - 1):
        i = wis[idx]
        rule = i.get('rule')
        if '>' in rule:
            k = '>='
            c, v = rule.split('>')
            v = int(v) + 1
            cmp = max
        else:
            k = '<'
            c, v = rule.split('<')
            v = int(v)
            cmp = min

        d = i.get('d')
        if d == 'A':
            final_rule = copy.deepcopy(new_rule)
            final_rule[c][k] = cmp(final_rule[c][k], v)
            rules.append(final_rule)
        elif d != 'R':
            old_val = new_rule[c][k]
            new_rule[c][k] = cmp(new_rule[c][k], v)
            possible_rules = get_paths(d, new_rule, instructions)
            rules.extend(possible_rules)
            new_rule[c][k] = old_val
        k, cmp = opp_map[k]
        new_rule[c][k] = cmp(new_rule[c][k], v)

    # Last part has no condition.
    d = wis[-1].get('d')
    if d == 'A':
        rules.append(copy.deepcopy(new_rule))
    elif d != 'R':
        possible_rules = get_paths(d, new_rule, instructions)
        rules.extend(possible_rules)
    return rules


def parse_data(data):
    rows = data.split('\n')
    return rows
