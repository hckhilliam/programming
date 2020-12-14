from collections import defaultdict
import functools
import math


def part1(data):
    rows = parse_data(data)
    t = int(rows[0])
    bids = set(rows[1].split(','))
    m = None
    bid = None
    for b in bids:
        if b == 'x':
            continue
        b = int(b)
        if not m:
            m = b - divmod(t, b)[1]
            bid = b
        elif (b - divmod(t, b)[1]) < m:
            m = b - divmod(t, b)[1]
            bid = b
    return bid * m


def part2(data):
    rows = parse_data(data)
    bids = [int(v) if v != 'x' else v for v in rows[1].split(',')]
    eqns = []
    currCh = 'a'
    for i, b in enumerate(bids):
        if b == 'x':
            continue
        eqns.append('{} * {} - {}'.format(b, currCh, i))
        currCh = chr(ord(currCh) + 1)
    return ' = '.join(eqns)  # Drop this value into wolfram alpha, find integer a for n = 0 lol.


def parse_data(data):
    rows = data.split('\n')
    return rows
