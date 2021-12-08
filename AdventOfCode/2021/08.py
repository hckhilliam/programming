from collections import defaultdict, deque
import functools
import math
import re


def part1(data):
    rows = parse_data(data)
    results = [d[1] for d in rows]
    total = 0
    for result in results:
        for r in result:
            c = len(r)
            if c == 2 or c == 3 or c == 4 or c == 7:
                total += 1
    return total


def part2(data):
    rows = parse_data(data)
    sum = 0
    for row in rows:
        sum += decode_row(row)
    return sum


def decode_row(row):
    # 1. Get A by difference between 7 and 1
    # 2. Get C or F by finding 1
    # 3. Get B or D by finding 4 and subtracting 1
    # 4. Get C or D or E by subtracting 8 from a 7seg
    # 5. -> find C by finding one with 2
    # 6. -> find D by finding one with 3
    # 7. -> find F by finding other 2
    # 8. -> find B by finding other 3 (C, D, F, B, A)
    # 9. -> find E by finding last one with 8
    # 10. -> find G by last letter avail
    segments = row[0]
    one = None
    four = None
    seven = None
    eight = None
    six_segs = []
    for s in segments:
        ss = set(s)
        if len(s) == 2:
            one = ss
        elif len(s) == 3:
            seven = ss
        elif len(s) == 4:
            four = ss
        elif len(s) == 7:
            eight = ss
        elif len(s) == 6:
            six_segs.append(ss)

    a = seven - one
    b = None
    c = None
    d = None
    e = None
    f = None
    bd = four - one
    for s in six_segs:
        letter = list(eight - set(s))[0]
        if letter in one:
            c = set(letter)
            f = one - c
        elif letter in bd:
            d = set(letter)
            b = bd - d
        else:
            e = set(letter)

    code_to_num = (
        (eight - d, '0'),
        (one, '1'),
        (eight - b - f, '2'),
        (eight - b - e, '3'),
        (four, '4'),
        (eight - c - e, '5'),
        (eight - c, '6'),
        (seven, '7'),
        (eight, '8'),
        (eight - e, '9')
    )

    results = row[1]
    number = ''
    for r in results:
        ss = set(r)
        for cn in code_to_num:
            if ss == cn[0]:
                number += cn[1]
                break
    return int(number)


def parse_data(data):
    rows = data.split('\n')
    data = []
    for r in rows:
        signals, results = r.split(' | ')
        data.append((signals.split(' '), results.split(' ')))
    return data
