from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c = 0
        j = 0
        for n in nums:
            if not n:
                c += 1
            else:
                nums[j] = n
                j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1

x = [0,1,0,3,12]
Solution().moveZeroes(x)
print(x)
