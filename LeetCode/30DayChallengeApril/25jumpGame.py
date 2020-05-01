from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        l = nums[0]
        for i in range(1, len(nums)):
            if l < i:
                return False
            l = max(l, nums[i] + i)

        return True
