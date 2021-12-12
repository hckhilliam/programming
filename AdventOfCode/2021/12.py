from collections import defaultdict, deque
import functools
import math
import re


class Cave(object):
    def __init__(self, name, is_big):
        self.name = name
        self.is_big = is_big
        self.neighbours = []


def part1(data):
    graph = parse_data(data)
    return find_distinct_paths('start', 'end', graph, {'start'})


def find_distinct_paths(start, end, graph, visited):
    if start == end:
        return 1

    total_paths = 0
    for n in graph[start].neighbours:
        cave = graph[n]
        if n not in visited:
            if not cave.is_big:
                visited.add(n)
            total_paths += find_distinct_paths(n, end, graph, visited)
            if n in visited:
                visited.remove(n)
    return total_paths


def part2(data):
    graph = parse_data(data)
    total_paths = find_distinct_paths2('start', 'end', graph, {'start'}, False)
    return total_paths


def find_distinct_paths2(start, end, graph, visited, small_visited):
    if start == end:
        return 1

    total_paths = 0
    for n in graph[start].neighbours:
        cave = graph[n]
        if n not in visited:
            if not cave.is_big:
                visited.add(n)
            total_paths += find_distinct_paths2(n, end, graph, visited, small_visited)
            if n in visited:
                visited.remove(n)
        elif n != 'start' and not small_visited:
            total_paths += find_distinct_paths2(n, end, graph, visited, True)
    return total_paths


def parse_data(data):
    rows = data.split('\n')

    graph = {}

    for r in rows:
        n1, n2 = r.split('-')
        cave1 = graph.get(n1)
        cave2 = graph.get(n2)
        if not cave1:
            cave1 = Cave(name=n1, is_big=n1 == n1.upper())
        if not cave2:
            cave2 = Cave(name=n2, is_big=n2 == n2.upper())
        cave1.neighbours.append(n2)
        cave2.neighbours.append(n1)
        graph[n1] = cave1
        graph[n2] = cave2
    return graph
