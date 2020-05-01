from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for sh in shift:
            if sh[0] == 0:
                s = s[sh[1]:] + s[:sh[1]]
            else:
                p = len(s) - sh[1]
                s = s[p:] + s[:p]
        return s
