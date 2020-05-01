class Solution:
    def singleNumber(self, nums):
      single = 0
      for n in nums:
        single ^= n
      return single

print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
