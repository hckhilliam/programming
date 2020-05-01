from collections import defaultdict
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # [1, 1], [1, 4], [2, 3], [3, 2], [4, 1], [5, 3]
        points.sort(key=lambda p: p[0])

        m = 0
        for i, p in enumerate(points):
            slopes = defaultdict(int)
            same = 1
            for j in range(i + 1, len(points)):
                dy = points[j][1] - p[1]
                dx = points[j][0] - p[0]
                if dy == 0 and dx == 0:
                    same += 1
                    continue
                if dy == 0:
                    dx = 1
                elif dx == 0:
                    dy = 1
                else:
                    gd = math.gcd(dy, dx)
                    dy //= gd
                    dx //= gd
                slopes[(dy, dx)] += 1
            m = max(m, (max(slopes.values()) if slopes else 0) + same)
        return m
