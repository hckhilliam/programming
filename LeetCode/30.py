from collections import deque, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        total_words = len(words)
        swords = defaultdict(int)
        for w in words:
            swords[w] += 1

        seen = defaultdict(int)
        l = deque([])

        wlen = len(words[0])
        indices = [] 
        for i in range(0, wlen):
            indices.extend(self.findSubstrings(i, s, wlen, swords, total_words))
        return indices

    def findSubstrings(self, i: int, s: str, wlen: int, swords: Dict[str, int], total_words: int) -> List[int]:
        indices = [] 
        c2 = i

        seen = defaultdict(int)
        l = deque([])
        while c2 < len(s):
            w = s[c2:c2 + wlen]
            if w not in swords:
                seen = defaultdict(int)
                l = deque([])
                c2 += wlen
                continue

            while seen[w] == swords[w]:
                r, _ = l.popleft()
                seen[r] -= 1

            seen[w] += 1
            l.append((w, c2))
            if len(l) == total_words:
                indices.append(l[0][1])
            c2 += wlen
        return indices
