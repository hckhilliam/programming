import heapq

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minh = []
        maxh = []
        s = 0
        m = 0
        for i, n in enumerate(nums):
            while maxh and minh and n > -maxh[0][0] and n - minh[0][0] > limit:
                s = heapq.heappop(minh)[1]
                while minh and minh[0][1] < s:
                    heapq.heappop(minh)
                s += 1
            while maxh and minh and n < minh[0][0] and -maxh[0][0] - n > limit:
                s = heapq.heappop(maxh)[1]
                while maxh and maxh[0][1] < s:
                    heapq.heappop(maxh)
                s += 1
            heapq.heappush(minh, (n, i))
            heapq.heappush(maxh, (-n, i))
            m = max(m, i - s + 1)
        return m
