from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    m_b = 14
    m_g = 13
    m_r = 12

    s = 0
    for r in rows:
        game, hands = r.split(': ')
        game = int(game.split(' ')[-1])
        valid = True
        for hand in hands.split('; '):
            parts = hand.split(', ')
            for p in parts:
                n, c = p.split(' ')
                if c == 'green' and int(n) > m_g:
                    valid = False
                    break
                elif c == 'red' and int(n) > m_r:
                    valid = False
                    break
                elif c == 'blue' and int(n) > m_b:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            s += game
    return s


def part2(data):
    rows = parse_data(data)

    s = 0
    for r in rows:
        game, hands = r.split(': ')
        game = int(game.split(' ')[-1])
        m_b = 0
        m_g = 0
        m_r = 0
        for hand in hands.split('; '):
            parts = hand.split(', ')
            for p in parts:
                n, c = p.split(' ')
                if c == 'green':
                    m_g = max(m_g, int(n))
                elif c == 'red':
                    m_r = max(m_r, int(n))
                elif c == 'blue':
                    m_b = max(m_b, int(n))
        s += m_b * m_g * m_r
    return s


def parse_data(data):
    rows = data.split('\n')
    return rows
