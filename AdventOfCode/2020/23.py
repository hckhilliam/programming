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
        for i, n in enumerate(nums):
            if n == dc:
                for j, s in enumerate(sides):
                    nums.insert((i + 1 + j) % len(nums), s)
                break
    return ''.join([str(i) for i in nums])


def part2(data):
    nums = deque([2, 5, 3, 1, 4, 9, 8, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    print(nums)
    track = set()
    nextTwo = set()
    for i in range(1000):
        # if tuple(nums) in track:
            # print('loop', i, nums)
        for j, n in enumerate(nums):
            if n == 1:
                t = (nums[(j + 1) % len(nums)], nums[(j + 2) % len(nums)])
                # if t in nextTwo:
                    # print('dupe', t, i)
                nextTwo.add(t)

        track.add(tuple(nums))
        cc = nums.popleft()
        sides = [nums.popleft() for i in range(3)]
        nums.append(cc)
        dc = (cc - 1) or 9
        while dc in sides:
            dc -= 1
            # Wrap.
            if dc == 0:
                dc = 9
        for i, n in enumerate(nums):
            if n == dc:
                for j, s in enumerate(sides):
                    nums.insert((i + 1 + j) % len(nums), s)
                break
    return ''.join([str(i) for i in nums])


def parse_data(data):
    rows = data.split('\n')
    return rows
