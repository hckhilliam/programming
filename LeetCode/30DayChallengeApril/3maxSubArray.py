from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # d[i] = max subarray including i and up to i
        # d[i] = max(d[i-1] + nums[i], nums[i])
        # max(d)
        pm = nums[0]
        m = nums[0]
        for i in range(1, len(nums)):
            pm = max(pm + nums[i], nums[i])
            m = max(pm, m)
        return m


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
