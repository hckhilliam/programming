from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        a = []
        for i, n in enumerate(nums):
            ind = index[i]
            a.insert(ind, n)
        return a
