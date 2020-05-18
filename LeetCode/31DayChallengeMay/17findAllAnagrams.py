class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = [0 for i in range(26)]
        a = ord('a')

        pc = [0 for i in range(26)]
        for ch in p:
            pc[ord(ch) - a] += 1

        j = 0
        b = 0
        r = []
        for i, ch in enumerate(s):
            c[ord(ch) - a] += 1
            if j == len(p):
                c[ord(s[b]) - a] -= 1
                b += 1
            else:
                j += 1
            if j == len(p) and c == pc:
                r.append(b)
        return r

