import numpy as np
from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        m = max(nums)
        a = [[1, i] for i in range(m + 1)]
        for i in range(2, m + 1):
            j = i * 2
            while j <= m:
                a[j].append(i)
                j += i

        s = 0
        for n in nums:
            if len(a[n]) == 4:
                s += sum(a[n])
        return s
