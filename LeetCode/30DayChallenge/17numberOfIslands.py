from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        for i, l in enumerate(grid):
            for j, v in enumerate(l):
                if v == '1':
                    self.sink(i, j, grid)
                    c += 1
        return c

    def sink(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.sink(i - 1, j, grid)
        self.sink(i + 1, j, grid)
        self.sink(i, j - 1, grid)
        self.sink(i, j + 1, grid)
