from collections import deque, defaultdict
import numpy as np
import scipy.spatial.transform as T


class Scanner(object):
    def __init__(self, i):
        self.i = i
        self.points = []
        self.relative_points = []
        self.final_points = None
        self.relative_location = None


def part1(data):
    scanners = parse_data(data)

    for i in range(1, len(scanners)):
        find_relative_points(scanners[i])

    scanners[0].final_points = set(scanners[0].points)
    finished_scanners = deque([scanners[0]])
    unfinished_scanners = {s:s for s in scanners[1:]}
    while unfinished_scanners:
        f_scanner = finished_scanners.popleft()
        for u_scanner in list(unfinished_scanners.values()):
            print(f'Finding match for scanner {u_scanner.i} to {f_scanner.i}')
            done = False
            for rotated_points in u_scanner.relative_points:
                for p1 in f_scanner.final_points:
                    for p2 in rotated_points:
                        dp = np.array([
                            p2[0] - p1[0],
                            p2[1] - p1[1],
                            p2[2] - p1[2]
                        ])
                        new_points = {tuple(pp - dp) for pp in rotated_points}
                        inter = new_points.intersection(f_scanner.final_points)
                        if len(inter) >= 12:
                            print(f'Found scanner {u_scanner.i}')
                            done = True
                            u_scanner.final_points = set(new_points)
                            finished_scanners.append(u_scanner)
                            unfinished_scanners.pop(u_scanner)
                            break
                    if done:
                        break
                if done:
                    break
            if not done:
                print(f'Couldnt find scanner {u_scanner.i}')
    all_beacons = scanners[0].final_points
    for i in range(1, len(scanners)):
        all_beacons = all_beacons.union(scanners[i].final_points)
    return len(all_beacons)


def part2(data):
    scanners = parse_data(data)

    for i in range(1, len(scanners)):
        find_relative_points(scanners[i])

    scanners[0].final_points = set(scanners[0].points)
    scanners[0].relative_location = np.array([0, 0, 0])
    finished_scanners = deque([scanners[0]])
    unfinished_scanners = {s:s for s in scanners[1:]}
    while unfinished_scanners:
        f_scanner = finished_scanners.popleft()
        for u_scanner in list(unfinished_scanners.values()):
            print(f'Finding match for scanner {u_scanner.i} to {f_scanner.i}')
            done = False
            for rotated_points in u_scanner.relative_points:
                for p1 in f_scanner.final_points:
                    for p2 in rotated_points:
                        dp = np.array([
                            p2[0] - p1[0],
                            p2[1] - p1[1],
                            p2[2] - p1[2]
                        ])
                        new_points = {tuple(pp - dp) for pp in rotated_points}
                        inter = new_points.intersection(f_scanner.final_points)
                        if len(inter) >= 12:
                            print(f'Found scanner {u_scanner.i}')
                            done = True
                            u_scanner.final_points = set(new_points)
                            u_scanner.relative_location = dp
                            finished_scanners.append(u_scanner)
                            unfinished_scanners.pop(u_scanner)
                            break
                    if done:
                        break
                if done:
                    break
            if not done:
                print(f'Couldnt find scanner {u_scanner.i}')

    max_dist = 0
    for i in range(len(scanners)):
        for j in range(i + 1, len(scanners)):
            delta = (scanners[i].relative_location - scanners[j].relative_location)
            max_dist = max(abs(delta[0]) + abs(delta[1]) + abs(delta[2]), max_dist)
    return max_dist


def parse_data(data):
    rows = data.split('\n')
    scanner_i = 0
    scanner = Scanner(scanner_i)
    scanners = []
    i = 1
    while i < len(rows):
        # Blank space to start new scanner.
        if not rows[i]:
            scanners.append(scanner)
            scanner_i += 1
            scanner = Scanner(scanner_i)
            i += 1
        else:
            x, y, z = rows[i].split(',')
            scanner.points.append((int(x), int(y), int(z)))
        i += 1
    scanners.append(scanner)
    return scanners


def find_relative_points(scanner):
    z_axe = np.array([0, 0, 1])
    y_axe = np.array([0, 1, 0])
    x_axe = np.array([1, 0, 0])
    amounts = [0, 90, 180, 270]

    # Helps dedupe rotations we've already done.
    rotated_already = set()
    for x_rot in amounts:
        for y_rot in amounts:
            for z_rot in amounts:
                transformed_points = []
                for i, p in enumerate(scanner.points):
                    x_vec = np.radians(x_rot) * x_axe
                    y_vec = np.radians(y_rot) * y_axe
                    z_vec = np.radians(z_rot) * z_axe
                    rot_x = T.Rotation.from_rotvec(x_vec)
                    p = rot_x.apply(p)
                    rot_y = T.Rotation.from_rotvec(y_vec)
                    p = rot_y.apply(p)
                    rot_z = T.Rotation.from_rotvec(z_vec)
                    p = rot_z.apply(p)
                    p = tuple(round(c) for c in p)
                    # Already transformed.
                    if i == 0 and p in rotated_already:
                        break
                    else:
                        rotated_already.add(p)
                    transformed_points.append(p)
                if transformed_points:
                    scanner.relative_points.append(transformed_points)
