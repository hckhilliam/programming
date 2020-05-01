from typing import List
import numpy as np

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return [0]

        l = np.zeros(len(nums), dtype=int)
        r = np.zeros(len(nums), dtype=int)
        p = 1
        for i, n in enumerate(nums):
            if not n:
                break
            p *= n
            l[i] = p
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if not n:
                break
            p *= n
            r[i] = p
        m = np.zeros(len(nums), dtype=int)
        m[0] = r[1]
        m[-1] = l[-2]
        for i in range(1, len(nums) - 1):
            m[i] = l[i-1] * r[i + 1]
        return m
