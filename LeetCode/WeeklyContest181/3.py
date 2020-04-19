from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if len(grid) == 1 and len(grid[0]) == 1:
            return True

        d = {
            ('l', 1): 'r', # coming from, going to
            ('l', 3): 'd',
            ('l', 5): 'u',
            ('u', 2): 'd',
            ('u', 5): 'l',
            ('u', 6): 'r',
            ('r', 1): 'l',
            ('r', 4): 'd',
            ('r', 6): 'u',
            ('d', 2): 'u',
            ('d', 3): 'l',
            ('d', 4): 'r'
        }
        o = {
            'r': 'l',
            'l': 'r',
            'u': 'd',
            'd': 'u'
        }

        v = grid[0][0]
        if v == 1 or v == 6:
            return self.hasValidEnd('r', 1, 0, grid, d, o)
        elif v == 2 or v == 3:
            return self.hasValidEnd('d', 0, 1, grid, d, o)
        elif v == 4:
            return self.hasValidEnd('r', 1, 0, grid, d, o) or self.hasValidEnd('d', 0, 1, grid, d, o)

    def hasValidEnd(self, n, x, y, grid, d, o):
        while x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0]):
            v = grid[y][x]
            k = (o[n], v)

            if k not in d:
                return False
            elif y == len(grid) - 1 and x == len(grid[0]) - 1:
                return True

            n = d[k]
            if n == 'r':
                x += 1
            elif n == 'l':
                x -= 1
            elif n == 'u':
                y -= 1
            else:
                y += 1
        return False
