from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s

        heapq.heapify(stones)
        while stones:
            m = heapq.heappop(stones)
            if not stones:
                return -m
            n = heapq.heappop(stones)
            d = m - n
            if d:
                heapq.heappush(stones, m - n)
        return 0


print(Solution().lastStoneWeight([2,7,4,1,8,1]))
