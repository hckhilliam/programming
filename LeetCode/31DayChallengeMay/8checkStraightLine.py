import math

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = coordinates[0]
        dy, dx = self.getSlope(a, coordinates[1])
        if dy == 0:
            return all(coordinates[i][1] == a[1] for i in range(2, len(coordinates)))
        elif dx == 0:
            return all(coordinates[i][0] == a[0] for i in range(2, len(coordinates)))

        for i in range(2, len(coordinates)):
            s = self.getSlope(a, coordinates[i])
            if s[0] != dy or s[1] != dx:
                return False
        return True

    def getSlope(self, a, b):
        dy = abs(b[1] - a[1])
        dx = abs(b[0] - a[0])
        d = math.gcd(dy, dx)
        return (dy // d, dx // d)
