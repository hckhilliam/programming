from typing import List
import numpy as np

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # d[i][j] = min sum to get to end
        d = np.zeros((len(grid), len(grid[0])), dtype=int)
        d[len(grid) - 1][len(grid[0]) - 1] = grid[len(grid) - 1][len(grid[0]) - 1]

        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[i]) - 1, -1, -1):
                p = []
                if i + 1 < len(grid):
                    p.append(grid[i][j] + d[i + 1][j])
                if j + 1 < len(grid[0]):
                    p.append(grid[i][j] + d[i][j + 1])
                d[i][j] = min(p) if p else grid[i][j]
        return d[0][0]

print(Solution().minPathSum([[1]]))
print(Solution().minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
