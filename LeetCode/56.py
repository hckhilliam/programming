class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        merged = []
        nl, nr = intervals[0]
        i = 1
        while i < len(intervals):
            il, ir = intervals[i]
            if il > nr:
                merged.append([nl, nr])
                nl = il
                nr = ir
            else:
                nr = max(nr, ir)
            i += 1
        merged.append([nl, nr])

        return merged