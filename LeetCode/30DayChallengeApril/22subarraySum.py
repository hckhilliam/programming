from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        leftSumDict = defaultdict(int)
        s = 0
        for n in nums:
            s += n
            leftSumDict[s] += 1

        c = leftSumDict.get(k, 0)
        s = nums[0]
        for i in range(1, len(nums)):
            leftSumDict[s] -= 1
            c += leftSumDict.get(k + s, 0)
            s += nums[i]
        return c
