class Node(object):
    def __init__(self, key, val):
        self.p = None
        self.n = None
        self.v = val
        self.k = key


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}
        self.h = None
        self.t = None

    def get(self, key: int) -> int:
        n = self.d.get(key)
        if not n:
            return -1
        self.push_to_front(n)
        self.print()
        return n.v

    def put(self, key: int, value: int) -> None:
        n = self.d.get(key)
        if n:
            n.v = value
            self.push_to_front(n)
        else:
            n = Node(key, value)
            self.d[key] = n
            # Init case.
            if not self.h:
                self.h = n
                self.t = n
            else:
                n.n = self.h
                self.h.p = n
                self.h = n

            if len(self.d) > self.capacity:
                del self.d[self.t.k]
                self.t = self.t.p
                self.t.n = None
        self.print()

    def push_to_front(self, n):
        if n == self.h:
            return

        if n == self.t:
            self.t = n.p
        else:
            n.n.p = n.p

        n.p.n = n.n
        n.p = None
        n.n = self.h
        self.h.p = n
        self.h = n

    def print(self):
        t = self.h
        while t:
            print(t.v)
            t = t.n
        print()
        t = self.t
        while t:
            print(t.v)
            t = t.p
        print()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(2)
# obj.put(1, 1)
# obj.put(2, 2)
# print(obj.get(1))
# obj.put(3, 3)
# print(obj.get(2))

obj = LRUCache(1)
obj.put(2, 1)
obj.get(2)
obj.put(3,2)
obj.get(2)
obj.get(3)
