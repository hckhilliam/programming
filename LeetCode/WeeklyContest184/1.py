from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matchings = []
        for i, w in enumerate(words):
            for j, w2 in enumerate(words):
                if i == j:
                    continue
                if w in w2:
                    matchings.append(w)
                    break
        return matchings

print(Solution().stringMatching(["mass","as","hero","superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching(["blue","green","bu"]))
