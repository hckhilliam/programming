from typing import List

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        s = sum(nums)
        m = 0
        r = []
        for n in nums:
            m += n
            s -= n
            r.append(n)
            if m > s:
                return r
