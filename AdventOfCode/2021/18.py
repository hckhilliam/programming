from collections import defaultdict, deque
import functools
import math
import re


class Tree(object):
    def __init__(self):
        self.root = None
        self.values_front = None
        self.values_back = None
        self.nodes_front = None
        self.nodes_back = None


class Node(object):
    def __init__(self, level):
        self.value = None
        self.children = []
        self.v_left = None
        self.v_right = None
        self.n_left = None
        self.n_right = None
        self.level = level

    def __str__(self):
        if self.value is not None:
            return f'value: {self.value}'
        return f'children: {len(self.children)}'


def part1(data):
    rows = parse_data(data)
    trees = []
    for r in rows:
        trees.append(create_tree(r))

    base_tree = trees[0]
    for i in range(1, len(trees)):
        add_trees(base_tree, trees[i])
    return calculate_magnitude(base_tree.root)


def part2(data):
    rows = parse_data(data)
    max_sum = 0
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            tree = create_tree(rows[i])
            tree2 = create_tree(rows[j])
            add_trees(tree, tree2)
            max_sum = max(max_sum, calculate_magnitude(tree.root))
            tree = create_tree(rows[i])
            tree2 = create_tree(rows[j])
            add_trees(tree2, tree)
            max_sum = max(max_sum, calculate_magnitude(tree2.root))
    return max_sum


def add_trees(tree1, tree2):
    merge_trees(tree1, tree2)
    reduce_tree(tree1)


def merge_trees(base_tree, tree):
    new_root = Node(0)
    new_root.n_right = base_tree.root
    base_tree.root.n_left = new_root
    new_root.children = [base_tree.root, tree.root]

    base_tree.nodes_back.n_right = tree.nodes_front
    tree.nodes_front.n_left = base_tree.nodes_back
    base_tree.root = new_root
    base_tree.nodes_front = base_tree.root
    base_tree.nodes_back = tree.nodes_back

    base_tree.values_back.v_right = tree.values_front
    tree.values_front.v_left = base_tree.values_back
    base_tree.values_back = tree.values_back

    # First is new node.
    n = base_tree.nodes_front.n_right
    while n:
        n.level += 1
        n = n.n_right


def reduce_tree(tree):
    not_reduced = True
    while not_reduced:
        not_reduced = False
        curr_n = tree.nodes_front
        while curr_n:
            if curr_n.level == 4 and curr_n.children:
                # Explode.
                curr_n.value = 0
                v1 = curr_n.children[0]
                v2 = curr_n.children[1]
                curr_n.children = []

                # Fix v linked list.
                curr_n.v_left = v1.v_left
                curr_n.v_right = v2.v_right
                if v1.v_left:
                    v1.v_left.value += v1.value
                    v1.v_left.v_right = curr_n
                else:
                    tree.values_front = curr_n
                if v2.v_right:
                    v2.v_right.value += v2.value
                    v2.v_right.v_left = curr_n
                else:
                    tree.values_back = curr_n

                # Fix n linked list.
                curr_n.n_right = v2.n_right
                if v2.n_right:
                    v2.n_right.n_left = curr_n
                else:
                    tree.nodes_back = curr_n

                not_reduced = True
                break
            curr_n = curr_n.n_right

        if not_reduced:
            continue

        curr_n = tree.values_front
        while curr_n:
            if curr_n.value >= 10:
                # Split.
                n1 = Node(curr_n.level + 1)
                n1.value = math.floor(curr_n.value / 2)
                n2 = Node(curr_n.level + 1)
                n2.value = math.ceil(curr_n.value / 2)
                curr_n.value = None
                curr_n.children = [n1, n2]

                # fix n linked list.
                n1.n_left = curr_n
                n1.n_right = n2
                n2.n_left = n1
                n2.n_right = curr_n.n_right
                if curr_n.n_right:
                    curr_n.n_right.n_left = n2
                else:
                    tree.nodes_back = n2
                curr_n.n_right = n1

                # fix v linked list
                n1.v_left = curr_n.v_left
                n1.v_right = n2
                n2.v_left = n1
                n2.v_right = curr_n.v_right
                if curr_n.v_left:
                    curr_n.v_left.v_right = n1
                else:
                    tree.values_front = n1
                if curr_n.v_right:
                    curr_n.v_right.v_left = n2
                else:
                    tree.values_back = n2
                curr_n.v_left = None
                curr_n.v_right = None

                not_reduced = True
                break
            curr_n = curr_n.v_right


def calculate_magnitude(node):
    if node.value is not None:
        return node.value

    return (
        3 * calculate_magnitude(node.children[0]) +
        2 * calculate_magnitude(node.children[1])
    )


def parse_data(data):
    rows = data.split('\n')
    return rows


def create_tree(row):
    tree = Tree()
    _, tree.root = build_tree(0, row, tree, curr_level=0)
    return tree


def build_tree(i, row, tree, curr_level):
    n = Node(curr_level)
    if not tree.nodes_front:
        tree.nodes_front = n
    if tree.nodes_back:
        tree.nodes_back.n_right = n
        n.n_left = tree.nodes_back
    tree.nodes_back = n
    if (row[i] == '['):
        i, child1 = build_tree(i + 1, row, tree, curr_level + 1)
        n.children.append(child1)
        # i should be at a comma and we skip that.
        i, child2 = build_tree(i + 1, row, tree, curr_level + 1)
        n.children.append(child2)
        # i should be at a closing bracket now
    else:
        n.value = int(row[i])
        if not tree.values_front:
            tree.values_front = n
        if tree.values_back:
            tree.values_back.v_right = n
            n.v_left = tree.values_back
        tree.values_back = n
    return i + 1, n


def print_values(tree):
    n = tree.values_front
    values = []
    levels = []
    while n:
        values.append(str(n.value))
        levels.append(str(n.level))
        n = n.v_right
    print(','.join(values))
    print(','.join(levels))
    print()


def assert_nodes_equal(tree):
    back = tree.nodes_back
    backs = []
    while back:
        backs.append(back)
        back = back.n_left
    backs.reverse()

    front = tree.nodes_front
    fronts = []
    while front:
        fronts.append(front)
        front = front.n_right

    for i in range(len(fronts)):
        assert fronts[i] == backs[i]


def assert_values_equal(tree):
    back = tree.values_back
    backs = []
    while back:
        backs.append(back)
        back = back.v_left
    backs.reverse()

    front = tree.values_front
    fronts = []
    while front:
        fronts.append(front)
        front = front.v_right

    for i in range(len(fronts)):
        assert fronts[i] == backs[i]
