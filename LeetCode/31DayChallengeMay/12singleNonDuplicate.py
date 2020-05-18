class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Returns lower of value if cannot be found.
        l = 0
        h = len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            n = nums[m]
            if (
                (m % 2 == 0 and m >= 1 and nums[m - 1] == n)
                or (m % 2 == 1 and m < len(nums) - 1 and nums[m + 1] == n)
            ):
                h = m - 1
            else:
                l = m + 1

        return nums[l - 1]
