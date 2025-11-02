class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []

        nl, nr = newInterval
        i = 0
        while i < len(intervals):
            il, ir = intervals[i]
            if nl <= ir:
                break   
            merged.append(intervals[i])
            i += 1

        # Case interval is last
        if i >= len(intervals):
            merged.append(newInterval)
            return merged
            
        il, ir = intervals[i]
        # Case before interval
        if nr < il:
            merged.append(newInterval)
        # Case merge
        else:
            ml = min(nl, il)
            mr = max(nr, ir)
            i += 1
            while i < len(intervals):
                il, ir = intervals[i]
                if il > mr:
                    break
                mr = max(mr, ir)
                i += 1
            merged.append([ml, mr])

        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged