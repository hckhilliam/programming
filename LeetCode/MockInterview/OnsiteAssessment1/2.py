import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # d[i][j] = how many paths from here to bottom right
        # d[m-1][n-1] = 1

        d = np.zeros((m + 1, n + 1), dtype=int)
        d[-1][-2] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                d[i][j] = d[i + 1][j] + d[i][j + 1]

        return d[0][0]
