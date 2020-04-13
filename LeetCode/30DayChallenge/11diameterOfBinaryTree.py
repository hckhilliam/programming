# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.h = {}

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.setHeights(root)
        m = 0
        for k in self.h:
            d = 0
            if k.left:
                d += self.h[k.left]
            if k.right:
                d += self.h[k.right]
            m = max(m, d)
        return m

    def setHeights(self, r):
        if not r:
            return 0

        self.h[r] = max(self.setHeights(r.left), self.setHeights(r.right)) + 1
        return self.h[r]


a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.left.left.left = TreeNode(6)
a.left.right.left = TreeNode(7)
a.left.left.left.left = TreeNode(8)
a.left.right.left.right = TreeNode(9)
print(Solution().diameterOfBinaryTree(a))