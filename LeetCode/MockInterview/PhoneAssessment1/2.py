class Node(object):
    def __init__(self, v):
        self.v = v
        self.t = False
        self.k = {}

class Trie:

    def __init__(self):
        self.r = Node('')


    def insert(self, word: str) -> None:
        n = self.r
        for c in word:
            if c not in n.k:
                n.k[c] = Node(c)
            n = n.k[c]
        n.t = True



    def search(self, word: str) -> bool:
        n = self.r
        for c in word:
            if c not in n.k:
                return False
            n = n.k[c]
        return n.t


    def startsWith(self, prefix: str) -> bool:
        n = self.r
        for c in prefix:
            if c not in n.k:
                return False
            n = n.k[c]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
