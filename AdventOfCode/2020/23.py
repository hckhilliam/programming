from collections import deque


def part1(data):
    nums = deque([int(i) for i in data])
    for i in range(100):
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
        for j, n in enumerate(nums):
            if n == 1:
                print(nums[(j + 1) % len(nums)], nums[(j + 2) % len(nums)])

    return ''.join([str(i) for i in nums])


def part2(data):
    # nums = deque([int(i) for i in data])
    # for i in range(10, 1000001):
    #     nums.append(i)
    nums = deque([i for i in range(1, 101)])

    neighbours = set()
    for i in range(1000):
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
        if i % len(nums) == 0:
            print(nums)
        # for j, n in enumerate(nums):
        #     if n == 1:
        #         t = (nums[j - 3], nums[j - 2], nums[j - 1], nums[(j + 1) % len(nums)], nums[(j + 2) % len(nums)])
        #         if t not in neighbours:
        #             neighbours.add(t)
        #             print(t, i)

    return None


def parse_data(data):
    rows = data.split('\n')
    return rows
