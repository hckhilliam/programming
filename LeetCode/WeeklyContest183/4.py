import numpy as np
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        f = np.zeros(len(stoneValue) + 1, dtype=int)
        s = np.zeros(len(stoneValue) + 1, dtype=int)
        f[-2] = stoneValue[-1]

        for i in range(len(stoneValue) - 2, -1, -1):
            f[i] = stoneValue[i] + s[i + 1]
            s[i] = f[i + 1]
            if i + 1 < len(stoneValue):
                t = stoneValue[i] + stoneValue[i + 1] + s[i + 2]
                if t > f[i]:
                    f[i] = t
                    s[i] = f[i + 2]
            if i + 2 < len(stoneValue):
                t = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + s[i + 3]
                if t > f[i]:
                    f[i] = t
                    s[i] = f[i + 3]
        if f[0] > s[0]:
            return 'Alice'
        elif s[0] > f[0]:
            return 'Bob'
        return 'Tie'
