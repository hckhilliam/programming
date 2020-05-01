from typing import List
from collections import defaultdict
import numpy as np

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ag = defaultdict(list)
        for s in strs:
            a = np.zeros(26, dtype=int)
            for c in s:
                a[ord(c) - ord('a')] += 1
            ag[tuple(a)].append(s)
        return ag.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
