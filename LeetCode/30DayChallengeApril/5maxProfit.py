from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        s = 0
        l = prices[0]
        h = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                s += h - l
                l = prices[i]
                h = prices[i]
            else:
                l = min(l, prices[i])
                h = max(h, prices[i])
        s += h - l
        return s

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))
