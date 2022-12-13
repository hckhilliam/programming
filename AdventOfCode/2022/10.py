from collections import defaultdict, deque
import functools
import math
import re


def get_signal_strength(cycle, x):
    if (cycle - 20) % 40 == 0:
        return cycle * x
    return 0

def part1(data):
    rows = parse_data(data)

    cycle = 1
    x = 1
    signal_strength = 0
    for r in rows:
        signal_strength += get_signal_strength(cycle, x)
        if r == 'noop':
            cycle += 1
        else:
            cycle += 1
            signal_strength += get_signal_strength(cycle, x)
            cycle += 1
            x += int(r.split(' ')[-1])
    signal_strength += get_signal_strength(cycle, x)
    return signal_strength


class Picture(object):
    def __init__(self):
        self.picture = []
        self.curr_row = ''
        self.cycle = 1
        self.x = 2

    def calculate_pixel(self):
        if self.cycle > 40:
            self.cycle -= 40
            self.picture.append(self.curr_row)
            self.curr_row = ''
        if self.cycle in {self.x-1, self.x, self.x+1}:
            self.curr_row += '#'
        else:
            self.curr_row += '.'

    def process(self, rows):
        for r in rows:
            self.calculate_pixel()

            if r == 'noop':
                self.cycle += 1
            else:
                self.cycle += 1
                self.calculate_pixel()
                self.cycle += 1
                self.x += int(r.split(' ')[-1])
        self.calculate_pixel()
        return '\n' + '\n'.join(self.picture)


def part2(data):
    rows = parse_data(data)
    return Picture().process(rows)



def parse_data(data):
    rows = data.split('\n')
    return rows
