class FirstUnique:

    def __init__(self, nums: List[int]):
        self.s = set()
        self.d = {}
        self.h = None
        self.t = None
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        return self.h.v if self.h else -1

    def add(self, value: int) -> None:
        print('val: {}'.format(value))
        if value in self.d:
            n = self.d.pop(value)
            if n.n:
                n.n.p = n.p
            else:
                self.t = n.p
            if n.p:
                n.p.n = n.n
            else:
                self.h = n.n
        elif value not in self.s:
            self.s.add(value)
            n = Node(value)
            if not self.h:
                self.h = n
                self.t = n
            else:
                self.t.n = n
                n.p = self.t
                self.t = n
            self.d[value] = n

    def pp(self):
        print('forward')
        n = self.h
        while n:
            print(n.v)
            n = n.n
        print('reverse')
        n = self.t
        while n:
            print(n.v)
            n = n.p


class Node(object):
    def __init__(self, v):
        self.v = v
        self.n = None
        self.p = None


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
