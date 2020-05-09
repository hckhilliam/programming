class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {a[0] for a in paths}
        for p in paths:
            if p[1] not in starts:
                return p[1]
        return None
