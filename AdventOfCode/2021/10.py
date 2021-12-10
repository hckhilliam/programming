from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    s = 0
    for r in rows:
        pts = find_corrupted_points(r)
        s += pts
    return s


def part2(data):
    rows = parse_data(data)
    scores = []
    for r in rows:
        score = get_score(r)
        if score > 0:
            scores.append(score)
    scores.sort()
    return scores[int(len(scores) / 2)]


def get_score(r):
    chars = deque()

    for c in r:
        if c == ')':
            l = chars.pop()
            if l != '(':
                return 0
        elif c == ']':
            l = chars.pop()
            if l != '[':
                return 0
        elif c == '}':
            l = chars.pop()
            if l != '{':
                return 0
        elif c == '>':
            l = chars.pop()
            if l != '<':
                return 0
        else:
            chars.append(c)

    score = 0
    while chars:
        c = chars.pop()
        score *= 5
        if c == '(':
            score += 1
        elif c == '[':
            score += 2
        elif c == '{':
            score += 3
        else:
            score += 4
    return score


def find_corrupted_points(r):
    chars = deque()

    for c in r:
        if c == ')':
            l = chars.pop()
            if l != '(':
                return 3
        elif c == ']':
            l = chars.pop()
            if l != '[':
                return 57
        elif c == '}':
            l = chars.pop()
            if l != '{':
                return 1197
        elif c == '>':
            l = chars.pop()
            if l != '<':
                return 25137
        else:
            chars.append(c)
    return 0


def is_broken(bracket, brace, paren, car):
    return bracket + brace + paren + car < 0


def corrupted(bracket, brace, paren, car):
    return (bracket < 0 or brace < 0 or paren < 0 or car < 0) and (bracket + brace + paren + car > 0)


def parse_data(data):
    rows = data.split('\n')
    return rows
