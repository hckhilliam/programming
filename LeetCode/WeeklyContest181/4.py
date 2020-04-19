class Solution:
    def longestPrefix(self, s: str) -> str:
        print(len(s))
        m = ""
        for i in range(len(s)):
            pre = s[:i]
            if s.endswith(pre):
                m = pre
        return m
