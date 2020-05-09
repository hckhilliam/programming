import math

class Solution:
    def findComplement(self, num: int) -> int:
        bits = floor(math.log2(num))
        ones = int('1' * (bits + 1), 2)
        return num ^ ones
