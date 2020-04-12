from typing import List

class Node(object):
    def __init__(self, v):
        self.v = v
        self.n = None
        self.p = None

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        a = Node(1)
        c = a
        for i in range(2, m + 1):
            n = Node(i)
            c.n = n
            n.p = c
            c = n

        r = []
        for q in queries:
            c = a
            i = 0
            while c.v != q:
                c = c.n
                i += 1
            r.append(i)
            if i == 0:
                continue
            if c.p:
                c.p.n = c.n
            if c.n:
                c.n.p = c.p
            c.p = None
            c.n = a
            a.p = c
            a = c
        return r


print(Solution().processQueries([3,1,2,1], 5))
print(Solution().processQueries([4,1,2,2], 4))
print(Solution().processQueries([7,5,5,8,3], 8))
