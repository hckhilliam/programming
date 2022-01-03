from collections import deque


def part1(data):
    nums = deque([int(i) for i in data])
    for _ in range(100):
        cc = nums.popleft()
        sides = [nums.popleft() for i in range(3)]
        nums.append(cc)
        dc = (cc - 1) or 9
        while dc in sides:
            dc -= 1
            # Wrap.
            if dc == 0:
                dc = 9
        for j, n in enumerate(nums):
            if n == dc:
                for k, s in enumerate(sides):
                    nums.insert((j + 1 + k) % len(nums), s)
                break
    return ''.join([str(i) for i in nums])


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def part2(data):
    max_num = 1000000
    nodes = dict()
    first_node = None
    curr_node = None
    for i in data:
        n = Node(int(i))
        if curr_node:
            curr_node.right = n
            n.left = curr_node
        else:
            first_node = n
        nodes[n.value] = n
        curr_node = n
    for i in range(10, max_num + 1):
        n = Node(i)
        curr_node.right = n
        n.left = curr_node
        nodes[i] = n
        curr_node = n
    curr_node.right = first_node
    first_node.left = curr_node

    curr_node = first_node
    for _ in range(10000000):
        nn = curr_node.right
        sides = set()
        for _ in range(3):
            sides.add(nn.value)
            nn = nn.right

        dc = (curr_node.value - 1) or max_num
        while dc in sides:
            dc = (dc - 1) or max_num

        n = nodes[dc]
        moving_link_start = curr_node.right
        moving_link_end = nn.left
        r = n.right
        n.right = moving_link_start
        moving_link_start.left = n
        r.left = moving_link_end
        moving_link_end.right = r

        curr_node.right = nn
        nn.left = curr_node
        curr_node = nn

    first = nodes[1].right
    second = first.right
    return first.value * second.value


def parse_data(data):
    rows = data.split('\n')
    return rows
