import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        d = np.zeros((len(text1) + 1, len(text2) + 1), dtype=int)
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    d[i][j] = 1 + d[i + 1][j + 1]
                d[i][j] = max(d[i][j], max(d[i][j + 1], d[i + 1][j]))
        return d[0][0]


print(Solution().longestCommonSubsequence('abcde', 'ace'))
print(Solution().longestCommonSubsequence('abc', 'abc'))
print(Solution().longestCommonSubsequence('abc', 'def'))
