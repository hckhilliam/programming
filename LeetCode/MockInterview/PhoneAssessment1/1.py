class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = []
        for n in nums:
            e = [i for i in nums if i != n]
            tt = self.permute(e)
            t = [[n] + a for a in tt]
            p.extend(t)
        return p if p else [[]]
