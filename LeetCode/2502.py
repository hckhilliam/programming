from collections import defaultdict


class Node:
    def __init__(self, startInd, size):
        self.startInd = startInd
        self.size = size
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.startInd}: {self.size}"


class Allocator:
    # heap holding (i, size)
    # allocate will be searching heap
    # sorted intervals as a linkedlist
    # allocate: find next free and insert sorted intervals (o(n))
    # free: delete intervals that have mID (O(1) -- # of mID blocks)

    def __init__(self, n: int):
        self.size = n
        self.memory = None
        self.hash = defaultdict(list)

    def __print(self):
        currNode = self.memory
        p = []
        while currNode:
            p.append(str(currNode))
            currNode = currNode.next
        print(", ".join(p))

    def allocate(self, size: int, mID: int) -> int:
        if size > self.size:
            return -1

        node = self.__insertNode(size)
        if not node:
            return -1

        self.hash[mID].append(node)
        # self.__print()
        return node.startInd

    def __insertNode(self, size):
        if not self.memory:
            self.memory = Node(0, size)
            return self.memory

        currNode = self.memory
        currInd = 0
        while True:
            # Found a fit.
            if currNode.startInd - currInd >= size:
                node = Node(currInd, size)
                node.next = currNode
                if currNode.prev:
                    node.prev = currNode.prev
                    currNode.prev.next = node
                else:
                    self.memory = node
                currNode.prev = node
                return node
            else:
                currInd = currNode.startInd + currNode.size

            # End of LL.
            if not currNode.next:
                if currInd + size > self.size:
                    return None
                node = Node(currInd, size)
                node.prev = currNode
                currNode.next = node
                return node
            currNode = currNode.next

    def freeMemory(self, mID: int) -> int:
        if mID not in self.hash:
            return 0

        numFreed = 0
        for node in self.hash[mID]:
            numFreed += node.size
            self.__deleteNode(node)

        del self.hash[mID]
        # self.__print()
        return numFreed

    def __deleteNode(self, node):
        p = node.prev
        n = node.next
        if p:
            p.next = n
        else:
            self.memory = n
        if n:
            n.prev = p


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)
