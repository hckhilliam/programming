import numpy as np
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c = 0
        f = {}
        m = 0
        for i, n in enumerate(nums):
            if n:
                c += 1
            else:
                c -= 1
            if c == 0:
                m = max(m, i + 1)
            if c not in f:
                f[c] = i
            else:
                m = max(m, i - f[c])
        return m
