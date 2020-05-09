from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums) // 2 + 1
        cnts = defaultdict(int)
        for n in nums:
            cnts[n] += 1
            if cnts[n] >= c:
                return n
        return None
