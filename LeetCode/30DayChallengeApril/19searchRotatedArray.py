from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = nums[0]
        l = 0
        h = len(nums)
        b = h // 2

        # Binary search index of rotation.
        while b != l:
            if nums[b] > n:
                l = b
                b = (b + h) // 2
            else:
                h = b
                b = (b + l) // 2

        # Binary search shifting by # indices rotated.
        b = (b + 1) % len(nums)
        l = 0
        h = len(nums)
        c = h // 2
        while c != l:
            nn = nums[(c + b) % len(nums)]
            if nn > target:
                h = c
                c = (c + l) // 2
            else:
                l = c
                c = (c + h) // 2
        i = (c + b) % len(nums)
        return i if nums[i] == target else -1
