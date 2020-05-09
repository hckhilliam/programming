class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True

        li = - k - 1
        for i, n in enumerate(nums):
            if n == 1:
                if i - li <= k:
                    return False
                li = i
        return True
