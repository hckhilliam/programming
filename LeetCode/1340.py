from typing import List
import numpy as np
import heapq

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # d[i][k] = max indices u can visit starting at i, and max length d
        # d[i][k] = max(d[j][k]) for all j where arr[j] < arr[i]
        # d[l] = 1
        dp = np.zeros(len(arr), dtype=int)
        h = [(n, i) for i, n in enumerate(arr)]
        heapq.heapify(h)
        while h:
            n, i = heapq.heappop(h)
            m = 0
            j = i - 1
            while j >= 0 and j >= i - d and arr[j] < n:
                m = max(m, dp[j])
                j -= 1
            j = i + 1
            while j < len(arr) and j <= i + d and arr[j] < n:
                m = max(m, dp[j])
                j += 1
            dp[i] = 1 + m
        return max(dp)

print(Solution().maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2))
print(Solution().maxJumps([3,3,3,3,3], 3))
print(Solution().maxJumps([7,6,5,4,3,2,1], 1))
print(Solution().maxJumps([7,1,7,1,7,1], 2))
print(Solution().maxJumps([66], 1))