class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        s = {j for j in J}
        return sum(1 for i in S if i in s)
