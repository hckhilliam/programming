from collections import defaultdict, deque
import functools
import math
import re
import heapq
from utils import p_rows, to_array
import sys
from abc import ABC, abstractmethod

debug = False

class Module(ABC):
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    @abstractmethod
    def send_pulse(self, name, pulse):
        pass


class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.on = False

    def send_pulse(self, name, pulse):
        if pulse:
            return None

        self.on = not self.on
        return self.on


class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.memory = {}

    def send_pulse(self, name, pulse):
        self.memory[name] = pulse

        if all(self.memory.values()):
            return False
        return True


class Broadcaster(Module):
    def send_pulse(self, name, pulse):
        return pulse


def part1(data):
    rows = parse_data(data)
    num_pulses = {
        # Low.
        False: 0,
        # High.
        True: 0
    }
    m = {}
    for r in rows:
        n , outputs = r.split(' -> ')
        outputs = outputs.split(', ')
        if n.startswith('%'):
            type = FlipFlop
            n = n[1:]
        elif n.startswith('&'):
            type = Conjunction
            n = n[1:]
        else:
            type = Broadcaster
        m[n] = type(n, outputs)

    # Fill memory.
    for module in m.values():
        for output in module.outputs:
            m2 = m.get(output)
            if isinstance(m2, Conjunction):
                m2.memory[module.name] = False

    for _ in range(1000):
        pulses = {
            False: 1, # Button press.
            True: 0
        }
        q = deque([('broadcaster', False, 'button')])
        while q:
            name, pulse, source = q.popleft()
            module = m.get(name)
            if not module:
                continue
            out_pulse = module.send_pulse(source, pulse)
            if debug:
                print(name, pulse, out_pulse, end='')
            if out_pulse is None:
                if debug:
                    print()
                continue
            for o in module.outputs:
                if debug:
                    print(f' {o}', end='')
                q.append((o, out_pulse, name))
                pulses[out_pulse] += 1
            if debug:
                print()
        num_pulses[True] += pulses[True]
        num_pulses[False] += pulses[False]
        if debug:
            print(_)
            print(pulses)
            print()

    return math.prod(num_pulses.values())


def part2(data):
    rows = parse_data(data)
    m = {}
    for r in rows:
        n , outputs = r.split(' -> ')
        outputs = outputs.split(', ')
        if n.startswith('%'):
            type = FlipFlop
            n = n[1:]
        elif n.startswith('&'):
            type = Conjunction
            n = n[1:]
        else:
            type = Broadcaster
        m[n] = type(n, outputs)

    # Fill memory.
    for module in m.values():
        for output in module.outputs:
            m2 = m.get(output)
            if isinstance(m2, Conjunction):
                m2.memory[module.name] = False

    # These are the inputs that need to be true to make rx true.
    inputs = {'qh', 'lt', 'bq', 'vz'}
    on_map = {i: 0 for i in inputs}
    i = 1
    found_each = False
    while not found_each:
        q = deque([('broadcaster', False, 'button')])
        while q:
            name, pulse, source = q.popleft()
            module = m.get(name)
            if name == 'rx':
                continue

            out_pulse = module.send_pulse(source, pulse)
            if out_pulse is None:
                continue

            if isinstance(module, Conjunction) and name in inputs and out_pulse:
                on_map[name] = i
                if all(on_map.values()):
                    found_each = True
                    break

            for o in module.outputs:
                q.append((o, out_pulse, name))
        i += 1

    lcm = 1
    for r in on_map.values():
        lcm = lcm * r // math.gcd(lcm, r)
    return lcm


def parse_data(data):
    rows = data.split('\n')
    return rows
